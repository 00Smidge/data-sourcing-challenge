import requests
import pandas as pd
import json
import logging


def fetch_data(url: str, params: dict = {}, jdumps: bool = False):
    """
    Fetch data from a given URL. Params are optional.
    Set jdumps to True to print the first result with an indent of 4.

    Args:
        url (str): The URL to fetch data from.
        params (dict): Optional query parameters for the request.
        jdumps (bool): Whether to pretty print the JSON response.

    Returns:
        dict: The JSON response from the URL if successful, None otherwise.
    """
    # check types
    if not isinstance(url, str):
        raise ValueError(f"ERROR: url!! Please provide a string. Could not read {url}")
    if not isinstance(params, dict):
        raise ValueError(
            f"ERROR: params!! Please provide a dictionary . Could not read {params}"
        )
    if not isinstance(jdumps, bool):
        raise ValueError(
            f"ERROR: jdumps!! Please provide a boolean. Could not read {jdumps}"
        )

    logging.info("Attempting to connect.")
    res = requests.get(url, params=params or None)

    if res.status_code != 200:
        raise ValueError(f"Connection Error!! Code: {res.status_code}")

    if jdumps is True:
        logging.info("Returning first result:")
        # json.dumps(res.json(), indent=4)

    logging.info("Successfully connected")
    return res.json()


def extract_activityID_from_dict(events: list):
    """
    Extracts activityID from a list of dictionaries.

    Args:
        events (list): A list of dictionaries with an 'activityID' key.

    Returns:
        list: A list of activityIDs, or 'ID ERROR!' if the key is missing.
    """
    # check type
    if not isinstance(events, list):
        raise ValueError(f"ERROR!!! Please provide a list. Could not read {events}")

    ids = []

    for e in range(len(events)):
        try:
            ids.append(events[e]["activityID"])
        except KeyError:
            ids.append("ID ERROR!")
    return ids


def expand_rows(df, column: str = "linkedEvents"):
    """
    Expands rows in a DataFrame by creating individual rows from a list of dictionaries.

    Args:
        df (pd.DataFrame): The DataFrame to expand.
        column (str): The column containing the list of dictionaries to expand.

    Returns:
        list: A list of expanded rows from the DataFrame.
    """
    # check type
    if not isinstance(df, pd.DataFrame):
        raise ValueError(
            "ERROR!! Please provide a pandas Dataframe. ```pd.Dataframe(df)```"
        )

    # check column exists
    if column not in df.columns:
        raise ValueError(
            f"ERROR: column!!! Column {column} does not exist in the provided Dataframe"
        )

    rows = []

    for i in range(len(df)):
        for e in df.iloc[i][column]:
            rows.append(e)

    return rows


def clean_up(df, eventType: str):
    """
    Cleans a DataFrame by modifying column names and types based on eventType.

    Args:
        df (pd.DataFrame): The DataFrame to clean.
        eventType (str): The event type to determine column names.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # check types
    if not isinstance(df, pd.DataFrame):
        raise ValueError(
            f"ERROR!! Please provide a pandas Dataframe. Could not read {df}"
        )
    if not isinstance(eventType, str):
        raise ValueError(
            f"ERROR!! Please provide a string for eventType. Could not read {eventType}"
        )

    # copy dataframe for cleaner control
    cdf = df.copy()

    # set variables
    act_id = f"{str.upper(eventType)}_ActivityID"
    new_start = f"startTime_{str.upper(eventType)}"
    evn_id = f"{str.lower(eventType)}ID"

    # check if act_id string exists
    if act_id not in cdf.columns:
        raise ValueError(
            f"ERROR: act_id!!! Could not find column name {str.upper(eventType)}_ActivityID"
        )

    # rename startTime and activityID columns
    if "startTime" in cdf.columns:
        cdf.startTime = pd.to_datetime(df.startTime)
        cdf = cdf.rename(
            columns={
                "startTime": new_start,
                "activityID": evn_id,
            }
        )

    # set id type to string
    cdf[act_id] = cdf[act_id].astype("string")
    cdf[evn_id] = cdf[evn_id].astype("string")

    # drop unneeded "linkedEvent" column
    cdf = cdf.drop("linkedEvents", axis=1)

    return cdf
