import pandas as pd
import numpy as np

def calculate_food_percentage(df):
    """
    Calculate percentage of spending on food.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    float
        Food spending percentage.
    """

    required_columns = {
        "Category",
        "Amount",
        "Transaction Type"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = df.copy()

    data = data[
        data["Transaction Type"]
        .str.upper()
        == "DEBIT"
    ]

    total_spend = data["Amount"].sum()

    if total_spend == 0:
        return 0.0

    food_categories = [
        "Food",
        "Restaurant",
        "Cafe",
        "Food Delivery"
    ]

    food_spend = (
        data[
            data["Category"]
            .isin(food_categories)
        ]["Amount"]
        .sum()
    )

    percentage = (
        food_spend / total_spend
    ) * 100

    return float(percentage)

def calculate_quick_commerce_percentage(df):
    """
    Calculate percentage of spending on quick commerce.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    float
        Quick commerce spending percentage.
    """

    required_columns = {
        "Category",
        "Amount",
        "Transaction Type"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = df.copy()

    data = data[
        data["Transaction Type"]
        .str.upper()
        == "DEBIT"
    ]

    total_spend = data["Amount"].sum()

    if total_spend == 0:
        return 0.0

    quick_categories = [
        "Quick Commerce"
    ]

    quick_spend = (
        data[
            data["Category"]
            .isin(quick_categories)
        ]["Amount"]
        .sum()
    )

    percentage = (
        quick_spend / total_spend
    ) * 100

    return float(percentage)

def calculate_ecommerce_percentage(df):
    """
    Calculate percentage of spending on e-commerce.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    float
        E-commerce spending percentage.
    """

    required_columns = {
        "Category",
        "Amount",
        "Transaction Type"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = df.copy()

    data = data[
        data["Transaction Type"]
        .str.upper()
        == "DEBIT"
    ]

    total_spend = data["Amount"].sum()

    if total_spend == 0:
        return 0.0

    shopping_categories = [
        "Shopping",
        "E-Commerce"
    ]

    shopping_spend = (
        data[
            data["Category"]
            .isin(shopping_categories)
        ]["Amount"]
        .sum()
    )

    percentage = (
        shopping_spend / total_spend
    ) * 100

    return float(percentage)

def calculate_investment_percentage(df):
    """
    Calculate percentage of spending on investments.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    float
        Investment spending percentage.
    """

    required_columns = {
        "Category",
        "Amount",
        "Transaction Type"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = df.copy()

    data = data[
        data["Transaction Type"]
        .str.upper()
        == "DEBIT"
    ]

    total_spend = data["Amount"].sum()

    if total_spend == 0:
        return 0.0

    investment_categories = [
        "Investment"
    ]

    investment_spend = (
        data[
            data["Category"]
            .isin(investment_categories)
        ]["Amount"]
        .sum()
    )

    percentage = (
        investment_spend / total_spend
    ) * 100

    return float(percentage)

def calculate_transport_percentage(df):
    """
    Calculate percentage of spending on transport.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    float
        Transport spending percentage.
    """

    required_columns = {
        "Category",
        "Amount",
        "Transaction Type"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = df.copy()

    data = data[
        data["Transaction Type"]
        .str.upper()
        == "DEBIT"
    ]

    total_spend = data["Amount"].sum()

    if total_spend == 0:
        return 0.0

    transport_categories = [
        "Transport"
    ]

    transport_spend = (
        data[
            data["Category"]
            .isin(transport_categories)
        ]["Amount"]
        .sum()
    )

    percentage = (
        transport_spend / total_spend
    ) * 100

    return float(percentage)

def calculate_late_night_food_percentage(df):
    """
    Calculate percentage of food spending
    between 9 PM and 2 AM.
    """

    required_columns = {
        "Time",
        "Category",
        "Amount",
        "Transaction Type"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = df.copy()

    data["Hour"] = (
        pd.to_datetime(
            data["Time"],
            format="%H:%M",
            errors="coerce"
        ).dt.hour
    )

    data = data.dropna(
        subset=["Hour"]
    )

    data["Hour"] = (
        data["Hour"]
        .astype(int)
    )

    data = data[
        data["Transaction Type"]
        .str.upper() == "DEBIT"
    ]

    food_categories = [
        "Food",
        "Restaurant",
        "Cafe",
        "Food Delivery"
    ]

    food = data[
        data["Category"].isin(food_categories)
    ]

    total_food = food["Amount"].sum()

    if total_food == 0:
        return 0.0

    late_hours = [21, 22, 23, 0, 1]

    late_food = food[
        food["Hour"].isin(late_hours)
    ]["Amount"].sum()

    percentage = (
        late_food / total_food
    ) * 100

    return float(percentage)

def detect_shopaholic(df):
    """
    Detect Shopaholic archetype.
    """

    percentage = calculate_ecommerce_percentage(df)

    return {
        "Archetype": "THE SHOPAHOLIC",
        "Matched": percentage > 15,
        "Metric": percentage,
        "Threshold": 15
    }

def detect_investor(df):
    """
    Detect Investor archetype.
    """

    percentage = calculate_investment_percentage(df)

    return {
        "Archetype": "THE INVESTOR",
        "Matched": percentage > 15,
        "Metric": percentage,
        "Threshold": 15
    }

def detect_late_night_snacker(df):
    """
    Detect Late Night Snacker archetype.
    """

    percentage = calculate_late_night_food_percentage(df)

    return {
        "Archetype": "THE LATE-NIGHT SNACKER",
        "Matched": percentage > 50,
        "Metric": percentage,
        "Threshold": 50
    }

def detect_cab_commuter(df):
    """
    Detect Cab Commuter archetype.
    """

    percentage = calculate_transport_percentage(df)

    return {
        "Archetype": "THE CAB COMMUTER",
        "Matched": percentage > 10,
        "Metric": percentage,
        "Threshold": 10
    }

def count_subscription_vendors(df):
    """
    Count unique subscription vendors.
    """

    required_columns = {
        "Category",
        "Vendor"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    subscriptions = df[
        df["Category"] == "Subscription"
    ]

    return int(
        subscriptions["Vendor"].nunique()
    )

def detect_subscription_lover(df):
    """
    Detect Subscription Lover archetype.
    """

    count = count_subscription_vendors(df)

    return {
        "Archetype": "THE SUBSCRIPTION LOVER",
        "Matched": count >= 5,
        "Metric": count,
        "Threshold": 5
    }

def detect_yolo_spender(df):
    """
    Detect YOLO Spender archetype.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
        YOLO Spender detection result.
    """

    rate = calculate_savings_rate(df)

    result = {
        "Archetype": "THE YOLO SPENDER",
        "Matched": bool(rate < 10),
        "Metric": float(rate),
        "Threshold": 10.0
    }

    return result


def detect_disciplined_saver(df):
    """
    Detect Disciplined Saver archetype.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
        Disciplined Saver detection result.
    """

    rate = calculate_savings_rate(df)

    result = {
        "Archetype": "THE DISCIPLINED SAVER",
        "Matched": bool(rate > 40),
        "Metric": float(rate),
        "Threshold": 40.0
    }

    return result

def calculate_savings_rate(df):
    """
    Calculate savings rate.
    """

    required_columns = {
        "Transaction Type",
        "Amount"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = df.copy()

    data["Transaction Type"] = (
        data["Transaction Type"]
        .astype(str)
        .str.upper()
    )

    income = (
        data[
            data["Transaction Type"] == "CREDIT"
        ]["Amount"]
        .sum()
    )

    expense = (
        data[
            data["Transaction Type"] == "DEBIT"
        ]["Amount"]
        .sum()
    )

    if income == 0:
        return 0.0

    savings = income - expense

    return float(
        (savings / income) * 100
    )

def detect_foodie(df):
    """
    Detect Foodie archetype.
    """

    percentage = calculate_food_percentage(df)

    return {
        "Archetype": "THE FOODIE",
        "Matched": percentage > 25,
        "Metric": percentage,
        "Threshold": 25
    }


def detect_quick_commerce_junkie(df):
    """
    Detect Quick Commerce Junkie archetype.
    """

    percentage = calculate_quick_commerce_percentage(df)

    return {
        "Archetype": "THE QUICK COMMERCE JUNKIE",
        "Matched": percentage > 15,
        "Metric": percentage,
        "Threshold": 15
    }

def generate_spending_archetypes(df):
    """
    Generate all spending archetypes.
    """

    archetypes = [
        detect_foodie(df),
        detect_quick_commerce_junkie(df),
        detect_shopaholic(df),
        detect_investor(df),
        detect_late_night_snacker(df),
        detect_cab_commuter(df),
        detect_subscription_lover(df),
        detect_yolo_spender(df),
        detect_disciplined_saver(df)
    ]

    matched = [
        item
        for item in archetypes
        if item["Matched"]
    ]

    metadata = {
        "total_archetypes": len(archetypes),
        "matched_archetypes": len(matched)
    }

    return {
        "transactions": df,
        "archetypes": archetypes,
        "matched_archetypes": matched,
        "metadata": metadata
    }