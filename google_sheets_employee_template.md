# Employee Daily Update Sheet (Google Sheets)

Use this structure in your Google Sheet:

1. Name
2. Job Title
3. Job Description
4. Start Hour
5. End Hour
6. Duration (Hours)

## Setup steps
1. Open Google Drive and create a new Google Sheet.
2. Add the six headers above in row 1.
3. Set columns **Start Hour** and **End Hour** to `Time` format.
4. In `F2`, use this formula and drag down:

```excel
=IF(OR(D2="",E2=""),"",(E2-D2)*24)
```

5. Set column **Duration (Hours)** to `Number` with 2 decimals.

## Notes
- If a shift can cross midnight, use this instead in `F2`:

```excel
=IF(OR(D2="",E2=""),"",MOD(E2-D2,1)*24)
```
