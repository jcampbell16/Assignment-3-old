# Jasmine Campbell 250886086

# Import Graphics

from happy_histogram import drawSimpleHistogram


# State names
p = 'Pacific'
m = 'Mountain'
c = 'Central'
e = 'Eastern'


# make a file checker definition
def file_check(file):
    try:
        lines = open(file, "r", encoding="utf-8")
        return lines
    except IOError:
        print('Error: No file found.')
        exit()
    except ValueError:
        print('Error: Value Error')
        exit()


# Make Happiness Score counter
def happiness_counter(location):
    total = 0
    for line in location:
        tweet_list = line.split()
        value = 0
        counter = 0
        for l in range(len(tweet_list)):
            tweet_list[l] = tweet_list[l].strip('.').strip(',')
            if tweet_list[l] in key:
                counter += 1
                if tweet_list[l] in poswords:
                    value += 10
                if tweet_list[l] in okwords:
                    value += 5
                if tweet_list[l] in badwords:
                    value += 1
        if counter != 0:
            total += value/counter
        else:
            total += 0
    if len(location) != 0:
        final = "%.3f" % (total/len(location))
    else:
        final = 0
    return final


# Make final printing, so no long repeating occurs
def final_print(first_letter, loc):
    print('\nThe number of tweets in the {} zone are {}.The "happiness score" is {}.'.format(first_letter, len(loc), happiness_counter(loc)))


# Input keyword file and check
filename = input("Please enter keywords file name: ")
keywords = file_check(filename)

key = []
sent = []

# Separate keyword for its sentiment value and store
for line in keywords:
    kwords = line.split(',')
    key.append(kwords[0])
    sent.append(int(kwords[1].strip()))
    if line == "":
        raise RuntimeError("End of file expected.")


# Establish lists for keyword types
poswords = []
okwords = []
badwords = []

# Separate keywords into their proper lists
for i in range(len(sent)):
    if sent[i] == 10:
        poswords.append(key[i])
    elif sent[i] == 5:
        okwords.append(key[i])
    elif sent[i] == 1:
        badwords.append(key[i])


# Get tweet file name and check
filename = input("Please enter the tweets file name: ")
infile = file_check(filename)

# Establish Tweets list and store
tweets = []

for line in infile:
    tweets.append(line)

# Establish lists for latitude and longitude
lat = []
long = []


# Time to split the tweets by location
for line in tweets:
    location = line.split()
    lat.append(float(location[0].strip('[').strip(',')))
    long.append(float(location[1].strip(',').strip(']')))


# Establish lists for timezones
pacific = []
mountain = []
central = []
eastern = []

# Separate the tweets by time zone and check if latitude is in zone
for i in range(len(long)-1):
    if 24.660845 < lat[i] < 49.189787:
        if -125.242264 < long[i] < -115.236438:
            tweetp = tweets[i].strip()
            pacific.append(tweetp)
        elif -115.236428 < long[i] < -101.998892:
            tweetm = tweets[i].strip()
            mountain.append(tweetm)
        elif -101.998892 < long[i] < -87.518395:
            tweetc = tweets[i].strip()
            central.append(tweetc)
        elif -87.518395 < long[i] < -67.444574:
            tweete = tweets[i].strip()
            eastern.append(tweete)

# Print results
final_print(p, pacific)
final_print(m, mountain)
final_print(c, central)
final_print(e, eastern)

# Create lists for graphic
eval = float(happiness_counter(eastern))
cval = float(happiness_counter(central))
mval = float(happiness_counter(mountain))
pval = float(happiness_counter(pacific))

# Call graphic
drawSimpleHistogram(eval, cval, mval, pval)

keywords.close()
infile.close()
