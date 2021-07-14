import re
star_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5'}

def slot_hotelstars(utt):
    if re.search(r"(zero|one|two|three|four|five) star(s)?",utt):
        token = re.sub(r"(\s)?star(s)?",'',re.search(r"(zero|one|two|three|four|five) star(s)?", utt).group())
        return f"stars={star_dict[token]}"
    
    if re.search(r"(0|1|2|3|4|5)-? ?star(s)?", utt):
        return f"stars={utt[re.search(r'(0|1|2|3|4|5)-? ?star(s)?', utt).span()[0]]}"

def slot_pricerange(utt):
    if re.search(r"(cheap)|(inexpensive)", utt):
        return "pricerange=cheap"
    
    if re.search(r"moderate(ly)?", utt):
        return "pricerange=moderate"
    
    if re.search(r"(luxury)|(expensive)|(high priced)", utt):
        return "pricerange=expensive"
    
    if re.search(r"([Dd]on't care about( the)? price( range)?)|([Aa]ny price range)", utt):
        return "pricerange=dontcare"

def slot_internet(utt):
    if re.search(r"((do(es)?(n(')?t| not)) care about ([Ii]nternet|[Ww][Ii]-?[Ff][Ii]))|(([Ii]nternet|[Ww][Ii]-?[Ff][Ii]) is optional)",utt):
        return "internet=dontcare"
    
    if re.search(r"(do(es)?(n(')?t| not))( (need|have)( (it )?to)?)? (include|have|want)( free)? ([Ii]nternet|[Ww][Ii]-?[Ff][Ii])", utt):
        return "internet=no"
    
    if re.search(r'[Ii]nternet|[Ww]i(-)?fi', utt):
        return "internet=yes"

def slot_parking(utt):
    if re.search(r"([Pp]arking ((do(es)?(n't| not) matter)|(is ((optional)|(not necessary)))))|((do(es)?(n't| not) care about( the)? parking))", utt):
        return "parking=dontcare"
    
    if re.search(r"do(es)?(n't| not) (((need|have)( to have)?)|(require))( a)?( free)? parking", utt):
        return "parking=no"
    
    if re.search(r'[Pp]arking', utt):
        return "parking=yes"

def slot_area(utt):
    if re.search(r"any(where| (area|part of town))", utt):
        return "area=dontcare"
    
    if re.search(r"[Cc]ent(re|er)", utt):
        return "area=centre"
    
    if re.search(r"([Ee]ast|[Ww]est|[Ss]outh|[Nn]orth)(ern)?", utt):
        ans = utt[re.search(r"([Ee]ast|[Ww]est|[Ss]outh|[Nn]orth)(ern)?", utt).span()[0]:re.search(r"([Ee]ast|[Ww]est|[Ss]outh|[Nn]orth)(ern)?", utt).span()[1]].lower().replace("ern","")
        return f"area={ans}"

def slot_hoteltype(utt):
    if re.search("[Gg]uest? ?house",utt):
        return "type=guesthouse"

    if re.search("[Hh]otel(s)?", utt) and re.search("[Gg]uest? ?house", utt):
        return "type=dontcare"
