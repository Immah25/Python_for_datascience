def download_csv(**csv_file):
    """
    Download one or more CSV files from provided URLs and save them locally.

    This function accepts keyword arguments where each key represents the
    desired output filename (without the `.csv` extension) and each value
    is a URL pointing to a CSV file. Each file is downloaded using pandas
    and saved in the current working directory.

    Parameters
    ----------
    **csv_file : dict
        Arbitrary keyword arguments mapping output file names to CSV URLs.
        Example:
            Animal_csv='https://example.com/data.csv'
    
    Returns
    -------
    None
        The function saves CSV files to disk and prints a success message.

    Raises
    ------
    pandas.errors.ParserError
        If the CSV file cannot be parsed.
    urllib.error.URLError
        If the URL is invalid or unreachable.
    """
    import pandas as pd
    for item, link in csv_file.items():
        csv = pd.read_csv(link)
        csv.to_csv(f"{item}.csv", index=False)
    print("Downloaded successfully!!")