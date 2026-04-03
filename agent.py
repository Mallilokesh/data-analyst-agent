def ask_agent(df, query):
    query = query.lower()

    numeric_cols = df.select_dtypes(include='number').columns

    if "columns" in query:
        return f"Columns in dataset: {list(df.columns)}"

    elif "total" in query or "sum" in query:
        return f"Total values:\n{df[numeric_cols].sum()}"

    elif "average" in query or "mean" in query:
        return f"Average values:\n{df[numeric_cols].mean()}"

    elif "max" in query:
        return f"Maximum values:\n{df[numeric_cols].max()}"

    elif "min" in query:
        return f"Minimum values:\n{df[numeric_cols].min()}"

    elif "count" in query:
        return f"Total rows: {len(df)}"

    elif "summary" in query or "describe" in query:
        return df.describe().to_string()

    elif "head" in query:
        return df.head().to_string()

    elif "correlation" in query:
        return df.corr().to_string()

    else:
        return "I can help with: columns, total, average, max, min, count, summary, correlation, charts."