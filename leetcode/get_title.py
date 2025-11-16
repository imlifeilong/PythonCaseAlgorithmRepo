import json
import time

import requests

session = requests.Session()


def main(offset, result):
    url = 'https://leetcode.cn/graphql/'
    headers = {
        "Host": "leetcode.cn",
        "Connection": "keep-alive",
        "Content-Length": "1528",
        "x-csrftoken": "tz0L6kxoBDQrC1Lnsi9GoPywQmZt2xTi",
        "authorization": "",
        "uuuserid": "4a33420f2d0c0ff0a109cde0a76ffff4",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "random-uuid": "5379b7a7-4d5e-0bad-649a-804625e302e2",
        "Accept": "*/*",
        "Origin": "https://leetcode.cn",
        "Referer": "https://leetcode.cn/problems/two-sum/description/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "gr_user_id=f8d1cd83-e5a0-45f7-b53f-c7c5dd4654fd; _bl_uid=5Um17g0pvC9nLdba3tngg2F26I1n; a2873925c34ecbd2_gr_last_sent_cs1=user2416; aliyungf_tc=ff606ec7eb1d88a341551117425db3aca40428c6b803f0b548b59800eb09e12e; sl-session=zOJJRWGeGWlGIcpnXp4z5Q==; Hm_lvt_f0faad39bcf8471e3ab3ef70125152c3=1761361055,1761918489,1761971876,1763200230; HMACCOUNT=8C504E02DECE1086; a2873925c34ecbd2_gr_session_id=a5bb5711-e6a1-47b0-b7b6-a8d5a9fa78fd; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=a5bb5711-e6a1-47b0-b7b6-a8d5a9fa78fd; a2873925c34ecbd2_gr_session_id_sent_vst=a5bb5711-e6a1-47b0-b7b6-a8d5a9fa78fd; csrftoken=tz0L6kxoBDQrC1Lnsi9GoPywQmZt2xTi; tfstk=gyYmFniSAnSXidabmfbjm2G4GgnRlZ_1CdUOBNBZ4TW5WnhfBOvMdpjwkCQVSOvwFoIOBtposLJBMGQ2S3aMOCTxGNhflI_17vHKJdAXGNGwMGSyo47PGQ5agOoRzmVYcFMKJ2d263RM-vKYSGDc117NgGzVUbffONyVbdWP465L3N7wQbfP96C4giW4z_W5_N547dRrZ16PgN7wQQll1bAU79YwPUks2pXg4EZJosjcLIW2MK8rairXGTcSaUxlm9zGEPzwrsAgvV8z-cBeAtIdLLu8oNAPsKBJL2zlzMxB61vmor7v43TfkUH3OivGHM85q-rVtZXcYES7TzRcb3YlkEk_AQdl3MbJ20MAXZvDA9sqVY9MZtpwogymeOKpwESkLYUkCGxB61vmorJF4xEzYkju5_l9zlZ10_1lpeRWlHiGezKZZbqIci55MvhoZlZ10_1lpbcuARsVNsHd.; _gid=GA1.2.772528865.1763205867; LEETCODE_SESSION=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiNTcwODUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImExMzNhYTA2YmY5YzlhMDMxNWMyODYyYzNlNjdjNDU5OGE2YTA0M2IyZTE1MmUzNzBkMjg3NDY3MTJhMWQ2NTYiLCJpZCI6NTcwODUsImVtYWlsIjoiMTM3NzIwMzI0MTBAMTYzLmNvbSIsInVzZXJuYW1lIjoidXNlcjI0MTYiLCJ1c2VyX3NsdWciOiJ1c2VyMjQxNiIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNuL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvdXNlcjI0MTYvYXZhdGFyXzE2OTM1NTIzNjgucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsImRldmljZV9pZCI6IjRhMzM0MjBmMmQwYzBmZjBhMTA5Y2RlMGE3NmZmZmY0IiwiaXAiOiIxMTEuMTguMjQ0LjIwIiwiX3RpbWVzdGFtcCI6MTc2MzIwNTg2Ni40MDk5NDM2LCJleHBpcmVkX3RpbWVfIjoxNzY1NzM4ODAwLCJ2ZXJzaW9uX2tleV8iOjB9.YRKpplweyFuVZvKrSLKHg6K2NQ_CArYcqTkCgcLQ0eQ; a2873925c34ecbd2_gr_cs1=user2416; _ga=GA1.1.280760932.1760753739; Hm_lpvt_f0faad39bcf8471e3ab3ef70125152c3=1763205973; _ga_PDVPZYN3CW=GS2.1.s1763205766$o8$g1$t1763205974$j36$l0$h0",
    }
    params = json.dumps({"query":"\n    query problemsetPanelQuestionList($filters: QuestionFilterInput, $searchKeyword: String, $sortBy: QuestionSortByInput, $categorySlug: String, $limit: Int, $skip: Int) {\n  problemsetPanelQuestionList(\n    filters: $filters\n    searchKeyword: $searchKeyword\n    sortBy: $sortBy\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n  ) {\n    questions {\n      id\n      titleSlug\n      title\n      translatedTitle\n      questionFrontendId\n      paidOnly\n      difficulty\n      topicTags {\n        name\n        slug\n        nameTranslated\n      }\n      status\n      isInMyFavorites\n      frequency\n      acRate\n    }\n    totalLength\n    finishedLength\n    panelName\n    hasMore\n  }\n}\n    ","variables":{"skip":offset,"limit":100,"categorySlug":"","filters":{"filterCombineType":"ALL","statusFilter":{"questionStatuses":[],"operator":"IS"},"difficultyFilter":{"difficulties":[],"operator":"IS"},"languageFilter":{"languageSlugs":[],"operator":"IS"},"topicFilter":{"topicSlugs":[],"operator":"IS"},"acceptanceFilter":{},"frequencyFilter":{},"frontendIdFilter":{},"lastSubmittedFilter":{},"publishedFilter":{},"companyFilter":{"companySlugs":[],"operator":"IS"},"positionFilter":{"positionSlugs":[],"operator":"IS"},"contestPointFilter":{"contestPoints":[],"operator":"IS"},"premiumFilter":{"premiumStatus":[],"operator":"IS"}},"searchKeyword":"","sortBy":{"sortField":"CUSTOM","sortOrder":"ASCENDING"},"options":{"enabled":True}},"operationName":"problemsetPanelQuestionList"})
    r = session.post(url=url, headers=headers, data=params)
    print(r.text)
    questions = r.json().get("data", {}).get("problemsetPanelQuestionList", {}).get("questions", [])
    # result = {}
    for q in questions:
        val = f"{q['questionFrontendId']}.{q['title'].replace(' ', '')}"
        key = f"{q['questionFrontendId']}.{q['translatedTitle']}"
        print(key, val)
        result[key] = val


if __name__ == '__main__':
    index = 42
    # result = {}
    # offset = 0
    # while index > 0:
    #     print(index)
    #     main(offset, result)
    #     offset += 100
    #     time.sleep(10)
    #     index -= 1
    # with open('question.json', 'w') as f:
    #     f.write(json.dumps(result, ensure_ascii=False))
