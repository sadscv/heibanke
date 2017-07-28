# coding=utf-8

from pymongo import MongoClient
from zhihu_oauth import ZhihuClient
from zhihu_oauth.zhcls import ActType
import json
import sys
import os


dataFile = os.path.join(sys.path[0], "data.txt")
mongoClient = MongoClient()
client = ZhihuClient()
client.login_in_terminal('sadscv@hotmail.com', 'sadsad')
client.save_token('token.pkl')
client.load_token('token.pkl')
db = mongoClient.zhihu
me = client.me()
activities = me.activities
print(dir(activities))
f = open(dataFile, 'a')
for act in me.activities:
    if act.type == ActType.VOTEUP_ANSWER:
        print('#'*80)
        data = {}
        data['answer_content'] = act.target.content
        data['answer_excerpt'] = act.target.excerpt
        vote_time = act.__dict__['_data']['created_time']
        data['vote_time'] = act.__dict__['_data']['created_time']
        data['question_title'] = act.target.question.title
        f.write("\n"+str(vote_time))
        print(vote_time)
f.close()




        # result = db.mine.insert_one(data)
        # if result:
        #     print('insert success,id: %s' % result.inserted_id)
    # if act.type == ActType.FOLLOW_TOPIC:
    #     object = act
    #     for item in object.__dict__.items():
    #         print(item)




# for act in me.activities:
#     if act.type == ActType.VOTEUP_ANSWER:
#         print(act.target.answer.suggest_edit)
