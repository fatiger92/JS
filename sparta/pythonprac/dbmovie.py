from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.s9m5n3l.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 퀴즈 1
# movie = db.movies.find_one({'title':'가버나움'})
# print(movie['star'])

# 퀴즈 2
# 내가 만든 답
# selected_movie = db.movies.find_one({'title':'가버나움'})
# movies = list(db.movies.find({},{'_id':False}))
#
# for movie in movies:
#     if selected_movie['star'] == movie['star']:
#         print(movie['title'])

# 스파르타 답
# target_movie = db.movies.find_one({'title':'가버나움'})
# target_star = target_movie['star']
#
# movies = list(db.movies.find({'star':target_star}))
#
# for movie in movies:
#     print(movie['title'])

# 퀴즈 3
db.movies.update_one({'title':'가버나움'},{'$set':{'star':0}})