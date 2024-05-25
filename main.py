import pandas as pd

def format_to_two(x):
    if pd.notnull(x):
        return '{:.2f}'.format(x)
    else:
        return ""

# Generate *3 empty lists to later create for future export
awr_import = []
awb_import = []
awc_import = []
import_lists = [awr_import, awb_import, awc_import]

# Generate *3 dfs for templates from CSVs
awr_templates = pd.read_csv("templates/AWR_TEMPLATES.CSV")
awb_templates = pd.read_csv("templates/AWB_TEMPLATES.CSV")
awc_templates = pd.read_csv("templates/AWC_TEMPLATES.CSV")

# Initialise list of template codes#
""" replace these with the AWD codes for your templates """
template_codes = ["BAS1", "MAS1", "MENGS1", "BAT1", "MENGT1"]

# Get list of AWD codes from CSV as DF; split into series by AWD template stored in dictionary
awd_codes_full = pd.read_csv("AWD_CODES.CSV")
awd_codes = {}
for code in template_codes:
    # awd_codes[code] = pd.DataFrame.loc[(awd_codes_full['Template'] == code)]
    awd_codes[code] = awd_codes_full[awd_codes_full['Template'] == code]

awd_codes_series = {}
for code in template_codes:
    awd_codes_series[code] = awd_codes_full[awd_codes_full['Template'] == code]['Award code']
    
# For Loop 1 - for each template code
for code in template_codes:
    awr_t = awr_templates[awr_templates['Award code'] == code]
    awb_t = awb_templates[awb_templates['Award code'] == code]
    awc_t = awc_templates[awc_templates['Award code'] == code]
    templates = [awr_t, awb_t, awc_t]

    awds = awd_codes_series[code]

    # For Loop 2 - for each AWD code in associated series
    for awd in awds:

        # For Loop 3 - for each template
        for i in range(3):
            """ create copy of template, update 'Award code', add to existing DataFrame or add into list """
            df = templates[i].copy()

            # if AWR
            if i == 0:   
                df["Award Rule code"] = df["Award Rule code"].astype(str).str.zfill(4)

            # if AWB
            elif i == 1:
                df["Award Rule code"] = df["Award Rule code"].astype(str).str.zfill(4)
                df["Sequence number"] = df["Sequence number"].astype(str).str.zfill(3)
                df["Minimum credits"] = df["Minimum credits"].apply(format_to_two)
                df["Maximum credits"] = df["Maximum credits"].apply(format_to_two)
            
            # if AWC
            else:
                df["Marks"] = df["Marks"].apply(format_to_two)
                df["Marks.1"] = df["Marks.1"].apply(format_to_two)
                df["Marks.2"] = df["Marks.2"].apply(format_to_two)
                df["Rank"] = df["Rank"].astype(str).str.zfill(2)

            for inx, row in df.iterrows():
                row['Award code'] = awd
                import_lists[i].append(row)

# Convert lists to dataframes and export
awr_df = pd.DataFrame(awr_import)
awr_df.to_csv("output/import_AWRs.csv", index=False)
awb_df = pd.DataFrame(awb_import)
awb_df.to_csv("output/import_AWBs.csv", index=False)            
awc_df = pd.DataFrame(awc_import)
awc_df.to_csv("output/import_AWCs.csv", index=False)    

