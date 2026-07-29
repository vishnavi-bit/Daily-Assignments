def analyze_text(text):
    words = text.lower().split()
    unique_words=set(words)
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return {"unique_count":len(unique_words),"frequencies":freq} 