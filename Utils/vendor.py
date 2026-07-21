"""
Utility functions for vendor extraction and normalization.
"""

import re
import pandas as pd


def extract_vendor(description: str) -> str:
    """
    Extract the probable vendor name from a transaction description.
    """

    if pd.isna(description):
        return "UNKNOWN"

    description = str(description).strip().upper()

    prefixes = {
    "UPI",
    "NEFT",
    "IMPS",
    "RTGS",
    "BHIM",
    "ATM",
    "POS",
    "ECOM",
    "ACH",
    "NACH",
    "VISA",
    "MASTERCARD",
    "CARD",
    "DEBIT",
    "CREDIT",
    "PURCHASE",
    "PAYMENT",
    "TRANSFER",
    "MB",
    "IB",
    "MOB",
    "ONLINE",
    "INB",
    "MMT",
    "PG",
    "TXN"
}

    for prefix in prefixes:
        if description.startswith(prefix):
            description = description[len(prefix):]
            break

    description = description.split("@")[0]

    description = re.sub(r"\bREF[A-Z0-9]*\b", " ", description)
    description = re.sub(r"\bUTR[A-Z0-9]*\b", " ", description)
    description = re.sub(r"\bTXN[A-Z0-9]*\b", " ", description)

    description = re.sub(r"\d+", " ", description)
    description = re.sub(r"[^A-Z ]", " ", description)
    description = re.sub(r"\s+", " ", description).strip()

    if description == "":
        return "UNKNOWN"

    return description


def normalize_vendor_name(vendor: str) -> str:
    """
    Normalize extracted vendor names using predefined mapping rules.
    """

    if pd.isna(vendor):
        return "UNKNOWN"

    vendor = str(vendor).strip().upper()

    vendor_mapping = {
        "AMAZON SELLER SVCS": "AMAZON",
        "AMAZON PAY": "AMAZON",
        "AMZN": "AMAZON",

        "GOOGLE PAY": "GPAY",
        "GOOGLEPAY": "GPAY",
        "GPAY": "GPAY",

        "PHONEPE": "PHONEPE",
        "PHONE PE": "PHONEPE",

        "PAYTM": "PAYTM",

        "BHIM": "BHIM",

        "BLINKIT": "BLINKIT",
        "ZEPTO": "ZEPTO",
        "SWIGGY": "SWIGGY",
        "ZOMATO": "ZOMATO",

        "UBER": "UBER",
        "OLA": "OLA",

        "NETFLIX": "NETFLIX",
        "SPOTIFY": "SPOTIFY",
    }

    return vendor_mapping.get(vendor, vendor)


def normalize_vendors(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a normalized Vendor column from transaction descriptions.
    """

    df = df.copy()

    df["Vendor"] = (
        df["Description"]
        .apply(extract_vendor)
        .apply(normalize_vendor_name)
    )

    return df



"""
Utility functions for vendor extraction and normalization.
"""

import re
import pandas as pd


# ==========================================================
# Known Brand Mapping
# ==========================================================

KNOWN_BRANDS = {

    # ==========================================================
    # E-Commerce
    # ==========================================================
    "AMAZON": "AMAZON",
    "AMZN": "AMAZON",
    "AMAZON PAY": "AMAZON",
    "FLIPKART": "FLIPKART",
    "MYNTRA": "MYNTRA",
    "AJIO": "AJIO",
    "MEESHO": "MEESHO",
    "NYKAA": "NYKAA",
    "SHOPSY": "SHOPSY",
    "TATA CLIQ": "TATA CLIQ",
    "SNAPDEAL": "SNAPDEAL",
    "FIRSTCRY": "FIRSTCRY",
    "JIOMART": "JIOMART",

    # ==========================================================
    # Grocery & Food Delivery
    # ==========================================================
    "SWIGGY": "SWIGGY",
    "ZOMATO": "ZOMATO",
    "BLINKIT": "BLINKIT",
    "ZEPTO": "ZEPTO",
    "BIGBASKET": "BIGBASKET",
    "INSTAMART": "INSTAMART",
    "DUNZO": "DUNZO",
    "DMART": "DMART",
    "SPENCERS": "SPENCERS",
    "RELIANCE FRESH": "RELIANCE FRESH",
    "MORE": "MORE",

    # ==========================================================
    # Restaurants & Coffee
    # ==========================================================
    "MCDONALD": "MCDONALD'S",
    "MCDONALDS": "MCDONALD'S",
    "KFC": "KFC",
    "BURGER KING": "BURGER KING",
    "PIZZA HUT": "PIZZA HUT",
    "DOMINOS": "DOMINO'S",
    "DOMINO": "DOMINO'S",
    "SUBWAY": "SUBWAY",
    "STARBUCKS": "STARBUCKS",
    "BARBEQUE NATION": "BARBEQUE NATION",
    "HALDIRAM": "HALDIRAM",

    # ==========================================================
    # Ride Sharing
    # ==========================================================
    "UBER": "UBER",
    "OLA": "OLA",
    "RAPIDO": "RAPIDO",

    # ==========================================================
    # Payments
    # ==========================================================
    "PAYTM": "PAYTM",
    "PHONEPE": "PHONEPE",
    "PHONE PE": "PHONEPE",
    "GOOGLE PAY": "GPAY",
    "GOOGLEPAY": "GPAY",
    "GPAY": "GPAY",
    "BHIM": "BHIM",
    "MOBIKWIK": "MOBIKWIK",
    "FREECHARGE": "FREECHARGE",

    # ==========================================================
    # Banking
    # ==========================================================
    "HDFC": "HDFC BANK",
    "ICICI": "ICICI BANK",
    "SBI": "STATE BANK OF INDIA",
    "AXIS": "AXIS BANK",
    "KOTAK": "KOTAK MAHINDRA BANK",
    "INDUSIND": "INDUSIND BANK",
    "YES BANK": "YES BANK",
    "IDFC": "IDFC FIRST BANK",
    "FEDERAL": "FEDERAL BANK",

    # ==========================================================
    # Entertainment
    # ==========================================================
    "NETFLIX": "NETFLIX",
    "SPOTIFY": "SPOTIFY",
    "HOTSTAR": "DISNEY+ HOTSTAR",
    "DISNEY": "DISNEY+ HOTSTAR",
    "JIOCINEMA": "JIOCINEMA",
    "SONYLIV": "SONYLIV",
    "ZEE5": "ZEE5",
    "PRIME VIDEO": "AMAZON PRIME VIDEO",
    "AMAZON PRIME": "AMAZON PRIME VIDEO",
    "YOUTUBE": "YOUTUBE",
    "APPLE TV": "APPLE TV",

    # ==========================================================
    # Telecom
    # ==========================================================
    "AIRTEL": "AIRTEL",
    "JIO": "JIO",
    "BSNL": "BSNL",
    "VI": "VODAFONE IDEA",
    "VODAFONE": "VODAFONE IDEA",
    "IDEA": "VODAFONE IDEA",
        # ==========================================================
    # Utilities
    # ==========================================================
    "BESCOM": "BESCOM",
    "TANGEDCO": "TANGEDCO",
    "MSEB": "MSEB",
    "BWSSB": "BWSSB",
    "TORRENT POWER": "TORRENT POWER",
    "ADANI ELECTRICITY": "ADANI ELECTRICITY",
    "CESC": "CESC",
    "TATA POWER": "TATA POWER",

    # ==========================================================
    # Fuel
    # ==========================================================
    "INDIAN OIL": "INDIAN OIL",
    "IOCL": "INDIAN OIL",
    "HPCL": "HPCL",
    "BPCL": "BPCL",
    "SHELL": "SHELL",
    "NAYARA": "NAYARA ENERGY",
    "ESSAR": "ESSAR",

    # ==========================================================
    # Travel
    # ==========================================================
    "IRCTC": "IRCTC",
    "BOOKMYSHOW": "BOOKMYSHOW",
    "MAKEMYTRIP": "MAKEMYTRIP",
    "GOIBIBO": "GOIBIBO",
    "YATRA": "YATRA",
    "EASEMYTRIP": "EASEMYTRIP",
    "AIR INDIA": "AIR INDIA",
    "INDIGO": "INDIGO",
    "AKASA": "AKASA AIR",
    "SPICEJET": "SPICEJET",
    "VISTARA": "VISTARA",
    "CLEARTRIP": "CLEARTRIP",
    "REDBUS": "REDBUS",
    "ABHIBUS": "ABHIBUS",

    # ==========================================================
    # Hotels
    # ==========================================================
    "OYO": "OYO",
    "FABHOTELS": "FABHOTELS",
    "TREEBO": "TREEBO",
    "MARRIOTT": "MARRIOTT",
    "TAJ": "TAJ HOTELS",
    "ITC HOTELS": "ITC HOTELS",
    "LEMON TREE": "LEMON TREE",
    "GINGER": "GINGER",
    "RADISSON": "RADISSON",
    "NOVOTEL": "NOVOTEL",

    # ==========================================================
    # Pharmacy & Healthcare
    # ==========================================================
    "APOLLO": "APOLLO",
    "PHARMEASY": "PHARMEASY",
    "1MG": "TATA 1MG",
    "NETMEDS": "NETMEDS",
    "MEDPLUS": "MEDPLUS",
    "FORTIS": "FORTIS",
    "MAX HEALTHCARE": "MAX HEALTHCARE",
    "NARAYANA": "NARAYANA HEALTH",
    "MANIPAL": "MANIPAL HOSPITALS",
    "LAL PATHLABS": "LAL PATHLABS",
    "THYROCARE": "THYROCARE",

    # ==========================================================
    # Electronics
    # ==========================================================
    "CROMA": "CROMA",
    "RELIANCE DIGITAL": "RELIANCE DIGITAL",
    "VIJAY SALES": "VIJAY SALES",
    "SAMSUNG": "SAMSUNG",
    "APPLE": "APPLE",
    "MI": "XIAOMI",
    "XIAOMI": "XIAOMI",
    "ONEPLUS": "ONEPLUS",
    "LG": "LG",
    "SONY": "SONY",
    "BOSE": "BOSE",
    "DELL": "DELL",
    "HP": "HP",
    "LENOVO": "LENOVO",
    "ASUS": "ASUS",
        # ==========================================================
    # Education
    # ==========================================================
    "BYJUS": "BYJU'S",
    "BYJU": "BYJU'S",
    "UNACADEMY": "UNACADEMY",
    "COURSERA": "COURSERA",
    "UDEMY": "UDEMY",
    "SCALER": "SCALER",
    "CODING NINJAS": "CODING NINJAS",
    "GEEKSFORGEEKS": "GEEKSFORGEEKS",
    "UPGRAD": "UPGRAD",
    "SIMPLILEARN": "SIMPLILEARN",
    "GREAT LEARNING": "GREAT LEARNING",
    "EDX": "EDX",

    # ==========================================================
    # Cloud & Software
    # ==========================================================
    "MICROSOFT": "MICROSOFT",
    "GOOGLE": "GOOGLE",
    "OPENAI": "OPENAI",
    "CHATGPT": "OPENAI",
    "ADOBE": "ADOBE",
    "CANVA": "CANVA",
    "DROPBOX": "DROPBOX",
    "NOTION": "NOTION",
    "ZOOM": "ZOOM",
    "SLACK": "SLACK",
    "FIGMA": "FIGMA",
    "GITHUB": "GITHUB",
    "ATLASSIAN": "ATLASSIAN",
    "JIRA": "JIRA",
    "CONFLUENCE": "CONFLUENCE",
    "AWS": "AMAZON WEB SERVICES",
    "AZURE": "MICROSOFT AZURE",
    "DIGITALOCEAN": "DIGITALOCEAN",

    # ==========================================================
    # Logistics
    # ==========================================================
    "DELHIVERY": "DELHIVERY",
    "BLUE DART": "BLUE DART",
    "DTDC": "DTDC",
    "EKART": "EKART",
    "XPRESSBEES": "XPRESSBEES",
    "ECOM EXPRESS": "ECOM EXPRESS",
    "SHADOWFAX": "SHADOWFAX",
    "INDIA POST": "INDIA POST",

    # ==========================================================
    # Government
    # ==========================================================
    "FASTAG": "FASTAG",
    "NHAI": "NHAI",
    "GST": "GST",
    "INCOME TAX": "INCOME TAX",
    "EPFO": "EPFO",
    "ESIC": "ESIC",
    "PASSPORT": "PASSPORT SEVA",

    # ==========================================================
    # Investment & Trading
    # ==========================================================
    "GROWW": "GROWW",
    "ZERODHA": "ZERODHA",
    "KITE": "ZERODHA",
    "UPSTOX": "UPSTOX",
    "ANGEL ONE": "ANGEL ONE",
    "ANGEL": "ANGEL ONE",
    "ICICI DIRECT": "ICICI DIRECT",
    "MOTILAL": "MOTILAL OSWAL",
    "5PAISA": "5PAISA",
    "PAYTM MONEY": "PAYTM MONEY",

    # ==========================================================
    # Insurance
    # ==========================================================
    "LIC": "LIC",
    "SBI LIFE": "SBI LIFE",
    "HDFC LIFE": "HDFC LIFE",
    "ICICI PRUDENTIAL": "ICICI PRUDENTIAL",
    "MAX LIFE": "MAX LIFE",
    "TATA AIA": "TATA AIA",
    "BAJAJ ALLIANZ": "BAJAJ ALLIANZ",
    "STAR HEALTH": "STAR HEALTH",
    "NIVA BUPA": "NIVA BUPA",

    # ==========================================================
    # Retail & Fashion
    # ==========================================================
    "PANTALOONS": "PANTALOONS",
    "WESTSIDE": "WESTSIDE",
    "LIFESTYLE": "LIFESTYLE",
    "MAX FASHION": "MAX FASHION",
    "TRENDS": "RELIANCE TRENDS",
    "RELIANCE TRENDS": "RELIANCE TRENDS",
    "DECATHLON": "DECATHLON",
    "ZARA": "ZARA",
    "H&M": "H&M",
    "HM": "H&M",
    "LEVIS": "LEVI'S",
    "LEVI": "LEVI'S",
    "PUMA": "PUMA",
    "NIKE": "NIKE",
    "ADIDAS": "ADIDAS",
    "SKECHERS": "SKECHERS",

    # ==========================================================
    # Furniture & Home
    # ==========================================================
    "IKEA": "IKEA",
    "PEPPERFRY": "PEPPERFRY",
    "URBAN LADDER": "URBAN LADDER",
    "HOME CENTRE": "HOME CENTRE",

    # ==========================================================
    # Gaming
    # ==========================================================
    "STEAM": "STEAM",
    "EPIC GAMES": "EPIC GAMES",
    "PLAYSTATION": "PLAYSTATION",
    "PSN": "PLAYSTATION",
    "XBOX": "XBOX",
    "NINTENDO": "NINTENDO",
    "RIOT": "RIOT GAMES",
    "VALORANT": "RIOT GAMES",

    # ==========================================================
    # Social Media
    # ==========================================================
    "FACEBOOK": "META",
    "INSTAGRAM": "META",
    "WHATSAPP": "META",
    "META": "META",
    "SNAPCHAT": "SNAPCHAT",
    "LINKEDIN": "LINKEDIN",
    "TWITTER": "X",
    "X CORP": "X",
        # ==========================================================
    # Media & News
    # ==========================================================
    "TIMES OF INDIA": "TIMES OF INDIA",
    "HINDUSTAN TIMES": "HINDUSTAN TIMES",
    "THE HINDU": "THE HINDU",
    "INDIAN EXPRESS": "INDIAN EXPRESS",
    "ECONOMIC TIMES": "ECONOMIC TIMES",

    # ==========================================================
    # Automobile
    # ==========================================================
    "MARUTI": "MARUTI SUZUKI",
    "HYUNDAI": "HYUNDAI",
    "HONDA": "HONDA",
    "TATA MOTORS": "TATA MOTORS",
    "MAHINDRA": "MAHINDRA",
    "TOYOTA": "TOYOTA",
    "KIA": "KIA",
    "BMW": "BMW",
    "MERCEDES": "MERCEDES",
    "AUDI": "AUDI",

    # ==========================================================
    # Miscellaneous
    # ==========================================================
    "TATA": "TATA",
    "RELIANCE": "RELIANCE",
    "ADANI": "ADANI",
    "ITC": "ITC",
    "INFOSYS": "INFOSYS",
    "TCS": "TCS",
    "WIPRO": "WIPRO",
    "COGNIZANT": "COGNIZANT",
    "ACCENTURE": "ACCENTURE",
    "IBM": "IBM",
    "ORACLE": "ORACLE",
    "INTEL": "INTEL",
    "NVIDIA": "NVIDIA",
    "QUALCOMM": "QUALCOMM",

    # ==========================================================
    # Charity / NGO
    # ==========================================================
    "RED CROSS": "RED CROSS",
    "UNICEF": "UNICEF",
    "ISKCON": "ISKCON",
    "AKSHAYA PATRA": "AKSHAYA PATRA",

    # Food Delivery
    "BUNDL TECH": "SWIGGY",
    "BUNDL TECH P L": "SWIGGY",

    # Blinkit
    "GROFERS": "BLINKIT",
    "GROFERS INDIA": "BLINKIT",
    "GROFERS INDIA P L": "BLINKIT",

    # Ola
    "ANI TECHNOLOGIES": "OLA",

    # Rapido
    "ROPPEN": "RAPIDO",
    "ROPPEN TRANSPORTATION": "RAPIDO",

    # Zepto
    "KIRANAKART": "ZEPTO",
    "KIRANAKART TECH": "ZEPTO",

    # BMTC
    "TUMMOC": "TUMMOC",
    "BMTC": "BMTC",
}
def extract_vendor(description: str) -> str:
    """
    Clean transaction description and prepare it for vendor detection.
    """

    if pd.isna(description):
        return "UNKNOWN"

    description = str(description).upper().strip()

    prefixes = {
        "UPI",
        "NEFT",
        "IMPS",
        "RTGS",
        "BHIM",
        "ATM",
        "POS",
        "ECOM",
        "ACH",
        "NACH",
        "VISA",
        "MASTERCARD",
        "DEBIT",
        "CREDIT",
        "PURCHASE",
        "PAYMENT",
        "TRANSFER",
        "CARD",
    }

    # Replace common separators with spaces
    description = re.sub(r"[-_/]", " ", description)

    # Remove UPI IDs
    description = description.split("@")[0]

    # Remove digits
    description = re.sub(r"\d+", " ", description)

    # Remove special characters
    description = re.sub(r"[^A-Z ]", " ", description)

    # Remove extra spaces
    description = re.sub(r"\s+", " ", description).strip()

    words = description.split()

    # Remove prefixes only from the beginning
    while words and words[0] in prefixes:
        words.pop(0)

    description = " ".join(words)

    if not description:
        return "UNKNOWN"

    return description


def normalize_vendor_name(vendor: str) -> str:
    """
    Normalize vendor names using known brand keywords.
    """

    if pd.isna(vendor):
        return "UNKNOWN"

    vendor = str(vendor).upper().strip()

    for keyword in sorted(KNOWN_BRANDS.keys(), key=len, reverse=True):
        if keyword in vendor:
            return KNOWN_BRANDS[keyword]

    return vendor


def normalize_vendors(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a normalized Vendor column from transaction descriptions.
    """

    df = df.copy()

    df["Vendor"] = (
        df["Description"]
        .fillna("")
        .apply(extract_vendor)
        .apply(normalize_vendor_name)
    )

    return df