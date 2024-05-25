# AWD Record Populator, for use with SITS (Tribal Group)

Creates AWR, AWB, and AWC records based on templates. The created records are stored in the exact CSV format required for SITS upload.

*Designed to be used where multiple AWD records need AWRs, AWBs, and AWCs copied from an existing AWD record*

## Requirements

**1. A single template CSV file for each of AWR, AWB, and AWC records, using the following naming conventions:**
- AWR_TEMPLATES.CSV
- AWB_TEMPLATES.CSV
- AWC_TEMPLATES.CSV
- These files need to be stored locally in a "templates/" folder.
- There is no requirement to provide separate files for different AWD templates. All template records should be included in each file.

**2. A CSV file called "AWD_CODES.CSV" stored in the main directory.**
- This file should contain two columns: award code and template
- Award code should include the new AWD which requires records generated
- Template should reference the AWD code for the record to copy from
