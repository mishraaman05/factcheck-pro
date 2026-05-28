import re

def isolate_factual_claims(text: str) -> list:
    """
    Parses natural prose using regex structures to screen sentences 
    containing high density quantitative signals, statistical properties,
    and factual historical configurations.
    """
    if not text:
        return []

    # Segment blocks into sentences using structural delimiters
    raw_sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    unique_claims = []
    seen = set()

    # Evaluative filters matching target characteristics
    patterns = [
        r'\d+',                                      # Numeric assertions
        r'%\s*(?:percent)?',                         # Percentages
        r'\b(attain|freeze|boil|discover|found|conclude|revolve|orbit|grow|drop|increase|decrease)\b', # Action signals
        r'\b(century|years|dated|historical|scientific|research|study|statistics|data)\b',           # Context vectors
        r'\b(highest|lowest|fastest|slowest|maximum|minimum|chambers|elements|species)\b'            # Definitives
    ]
    combined_regex = re.compile('|'.join(patterns), re.IGNORECASE)

    # Exclusions
    noise_patterns = [
        r'\b(table of contents|toc|index|page \d+|all rights reserved|copyright|isbn)\b',
        r'^[\d\s\.\,\-\|]+$' # Structural line fragments
    ]
    noise_regex = re.compile('|'.join(noise_patterns), re.IGNORECASE)

    for sentence in raw_sentences:
        clean_sentence = sentence.strip().replace('\n', ' ')
        clean_sentence = re.sub(r'\s+', ' ', clean_sentence)
        
        # Validate minimum string complexity
        if len(clean_sentence) < 25 or len(clean_sentence) > 300:
            continue
            
        # Screen noise fragments
        if noise_regex.search(clean_sentence):
            continue
            
        # Check signature verification viability matching profiles
        if combined_regex.search(clean_sentence):
            norm_key = clean_sentence.lower().strip()
            if norm_key not in seen:
                seen.add(norm_key)
                unique_claims.append(clean_sentence)
                
    return unique_claims[:25]  # Safety bounding for operational stability