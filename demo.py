# gene variance
# gene evidences
# clinical trials
import numpy as np
import os
import pandas as pd
from openpyxl import load_workbook
folder = r"/home/gokulak/NewGene/MSK gene list - 660 genes"


gv_total = pd.DataFrame()
ge_total = pd.DataFrame()
ct_total = pd.DataFrame()
sheet6_total = pd.DataFrame()
sheet5_total = pd.DataFrame()
gene_summary_total = pd.DataFrame()
gene_associated_trials_total = pd.DataFrame()
variant_associated_tri_total = pd.DataFrame()
gene_asso_total = pd.DataFrame()

files = os.listdir(folder)
# print(files)

for file in files:
    if file.endswith(".xlsx"):
        # print(file)
        excel_file = pd.ExcelFile(f"{folder}/{file}")
        # print(excel_file)

        sheets = excel_file.sheet_names

        # print(f"{file}, {sheets}")
        print(sheets)
        for sheet in sheets:
            # print(sheet)
            # print(sheet)
            if sheet.lower().strip() == "gene variants":
                gv = excel_file.parse(sheet_name=sheet)
                gv_total = gv_total.append(gv)
                # print(gv_total.columns)

            elif sheet.lower().strip() == "gene evidences" or sheet.lower() == "gene level evidences":
                ge = excel_file.parse(sheet_name=sheet)
                ge_total = ge_total.append(ge)

            elif sheet.lower().strip() == "clinical trials":
                ct = excel_file.parse(sheet_name=sheet)
                ct_total = ct_total.append(ct)

            elif sheet.lower().strip() == "sheet6":
                sheet6 = excel_file.parse(sheet_name=sheet)
                sheet6_total = sheet6_total.append(sheet6)

            elif sheet.lower().strip() == "sheet5":
                sheet5 = excel_file.parse(sheet_name=sheet)
                sheet5_total = sheet5_total.append(sheet5)

            elif sheet.lower().strip() == "gene summary":
                gene_summary = excel_file.parse(sheet_name=sheet)
                gene_summary_total = gene_summary_total.append(gene_summary)

            elif sheet.lower().strip() == "gene associated trials (egfr ac":
                gene_associated_trials = excel_file.parse(sheet_name=sheet)
                gene_associated_trials_total = gene_associated_trials_total.append(
                    gene_associated_trials)

            elif sheet.lower().strip() == "variant associated clinical tri":
                variant_associated_tri = excel_file.parse(sheet_name=sheet)
                variant_associated_tri_total = variant_associated_tri_total.append(
                    variant_associated_tri)


# ge_total['GENE'] = ge_total.pop['GENE'].fillna(ge_total["GENE "]).astype(str)

ge_total["GENE"] = np.where(ge_total["GENE"].isna(
), ge_total["GENE "], ge_total["GENE"]).astype("str")

gv_total["GENE"] = np.where(gv_total["GENE"].isna(
), gv_total["GENE "], gv_total["GENE"]).astype("str")

# gv_total['GENE'] = gv_total['GENE'].replace(np.nan, 0)

gv_total["GENE"] = np.where(
    gv_total["GENE"].equals == np.nan, gv_total["gene"], gv_total["GENE"]).astype("str")

gv_total = gv_total.drop("GENE ", axis=1)


# gv_total["GENE"] = np.where(gv_total["GENE"].isnull(), 'value_is_NaN')
# , gv_total["gene"], gv_total["GENE"]).astype("str")


# gv_total['GENE'] = np.where(gv_total['GENE'].isna(
# ), gv_total["gene"], ge_total['GENE']).astype("str")

# gv_total['GENE'] = np.where(gv_total['GENE'].isna(
# ), gv_total["GENES"], ge_total['GENE']).astype("str")


# print(ge_total['GENE'])

with pd.ExcelWriter('combined660.xlsx') as writer:  # doctest: +SKIP
    gv_total.to_excel(writer, sheet_name='Gene Variants')
    ge_total.to_excel(writer, sheet_name='Gene Evidences')
