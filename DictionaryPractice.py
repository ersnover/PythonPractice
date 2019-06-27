phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#print(phonebook_dict['Elizabeth'])
#phonebook_dict['Kareem'] = '938-489-1234'
#del phonebook_dict['Alice']
#phonebook_dict['Bob'] = '968-345-2345'
#print(phonebook_dict)

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#print(ramit['email'])
#print(ramit['interests'][0])
#print(ramit['friends'][0]['email'])
#print(ramit['friends'][1]['interests'][1])

def letter_histogram():
  hist = {}
  word = input("Enter a word: ")
  for letter in word:
    try:
      type(hist[letter]) == int
      hist[letter] +=1
    except:
      hist[letter] = 1
  print(hist)

#letter_histogram()

def word_histogram():
  hist = {}
  sentence = input("Enter a sentence: ")
  sentence = sentence.split(" ")
  for word in sentence:
    try:
      type(hist[word]) == int
      hist[word] +=1
    except:
      hist[word] = 1
  print(hist)
  return hist

hist = word_histogram()

def histogram_count(histogram):
  top3 = [{"word": 0}, {"word": 0}, {"word": 0}]
  for newchar in histogram:
    i = 0
    for char in top3:
      if histogram[newchar] > top3[i][char]:
