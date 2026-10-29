"""Compute budget-vs-actual variances, KPIs and materiality flags from a monthly workbook.

Usage:
    python compute_variances.py <file.xlsx|file.csv> [--month Sep-26] [--pct 10] [--abs 5000] [--out result.json]

Input: a sheet (preferably "Monthly_Detail") with columns
    Month, Division, Line item, Type, Budget, Actual
Type is one of Revenue / Cost / Other / Below EBITDA. Costs are stored as negatives,
so Variance = Actual - Budget is favourable when positive for every line.
Prints a JSON summary; every figure comes from the source rows, nothing is estimated.
"""
import argparse, json, sys
import pandas as pd

COLS = ["Month", "Division", "Line item", "Type", "Budget", "Actual"]


def load(path):
    if path.lower().endswith(".csv"):
        frames = {"csv": pd.read_csv(path)}
    else:
        frames = pd.read_excel(path, sheet_name=None)
    order = sorted(frames, key=lambda n: n != "Monthly_Detail")
    for name in order:
        df = frames[name]
        df.columns = [str(c).strip() for c in df.columns]
        if all(c in df.columns for c in COLS):
            df = df[COLS].dropna(subset=["Month"])
            df["Budget"] = pd.to_numeric(df["Budget"], errors="coerce").fillna(0)
            df["Actual"] = pd.to_numeric(df["Actual"], errors="coerce").fillna(0)
            return df, name
    sys.exit(f"No sheet has the columns {COLS}. Found sheets: {list(frames)}")


def flag(df, pct, abs_t):
    df = df.copy()
    df["Variance"] = df["Actual"] - df["Budget"]
    df["Var_pct"] = df.apply(lambda r: None if r["Budget"] == 0 else r["Variance"] / abs(r["Budget"]), axis=1)
    df["Material"] = df.apply(
        lambda r: r["Variance"] != 0 and (abs(r["Variance"]) >= abs_t or (r["Var_pct"] is not None and abs(r["Var_pct"]) >= pct)), axis=1)
    df["F_A"] = df["Variance"].apply(lambda v: "F" if v > 0 else ("A" if v < 0 else "-"))
    df["IC"] = df["Line item"].str.contains(r"\(IC\)")
    return df


def kpis(df):
    out = {}
    groups = {"Revenue": df["Type"] == "Revenue", "Total costs": df["Type"] == "Cost",
              "EBITDA": df["Type"] != "Below EBITDA", "Net result": df["Type"].notna()}
    for k, m in groups.items():
        b, a = float(df.loc[m, "Budget"].sum()), float(df.loc[m, "Actual"].sum())
        out[k] = {"budget": b, "actual": a, "variance": a - b, "var_pct": None if b == 0 else (a - b) / abs(b)}
    return out


def period(df, months, month, ytd):
    if ytd:
        keep = months[: months.index(month) + 1]
        sub = df[df["Month"].isin(keep)]
    else:
        sub = df[df["Month"] == month]
    return sub.groupby(["Division", "Line item", "Type"], as_index=False)[["Budget", "Actual"]].sum()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path"); ap.add_argument("--month"); ap.add_argument("--pct", type=float, default=10)
    ap.add_argument("--abs", type=float, default=5000); ap.add_argument("--out")
    a = ap.parse_args()
    df, sheet = load(a.path)
    months = list(dict.fromkeys(df["Month"].astype(str)))
    df["Month"] = df["Month"].astype(str)
    month = a.month or months[-1]
    res = {"source_sheet": sheet, "rows": len(df), "period": month, "thresholds": {"pct": a.pct, "abs": a.abs}}
    for label, ytd in (("month", False), ("ytd", True)):
        p = flag(period(df, months, month, ytd), a.pct / 100, a.abs)
        res[label] = {"kpis": kpis(p),
                      "by_division_ebitda": p[p["Type"] != "Below EBITDA"].groupby("Division")[["Budget", "Actual"]].sum().assign(
                          Variance=lambda x: x["Actual"] - x["Budget"]).to_dict("index"),
                      "material": p[p["Material"]].sort_values("Variance", key=abs, ascending=False).to_dict("records")}
    trend = df[df["Type"] != "Below EBITDA"].groupby("Month", sort=False)[["Budget", "Actual"]].sum()
    res["ebitda_trend"] = trend.reindex(months).to_dict("index")
    # self-check: line totals tie to the source rows
    src = df[df["Month"] == month]
    assert abs(src["Actual"].sum() - res["month"]["kpis"]["Net result"]["actual"]) < 0.5, "Month totals do not tie"
    text = json.dumps(res, indent=2, default=float)
    if a.out:
        open(a.out, "w").write(text)
    print(text)


if __name__ == "__main__":
    main()
