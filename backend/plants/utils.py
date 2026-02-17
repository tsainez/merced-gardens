import requests

def fetch_gbif_data(name):
    """
    Fetches taxonomy data from GBIF API.
    Returns a dictionary with 'scientific_name', 'common_name', and 'rank' if found, else None.
    """
    base_url = "https://api.gbif.org/v1/species/match"
    params = {
        'name': name,
        'kingdom': 'Plantae',  # Restrict to plants
        'verbose': True
    }

    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get('matchType') == 'NONE':
            return None

        result = {
            'scientific_name': data.get('scientificName'),
            'canonical_name': data.get('canonicalName'),
            'rank': data.get('rank'),
            'usage_key': data.get('usageKey'),
            'common_name': None
        }

        # specific common name fetch
        if result['usage_key']:
            common_name_url = f"https://api.gbif.org/v1/species/{result['usage_key']}/vernacularNames"
            cn_response = requests.get(common_name_url, timeout=5)
            if cn_response.status_code == 200:
                cn_data = cn_response.json()
                # Try to find an English common name
                english_names = [n['vernacularName'] for n in cn_data.get('results', []) if n.get('language') == 'eng']
                if english_names:
                    result['common_name'] = english_names[0]

        return result

    except requests.RequestException as e:
        print(f"Error fetching GBIF data: {e}")
        return None
