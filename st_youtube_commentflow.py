import streamlit as st
from chat_downloader import ChatDownloader
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

st.title('YouTube 配信コメント流量分析')
input_url = st.sidebar.text_input('ここに動画のURLを入れてください')

search = st.sidebar.radio('検索方法',
            			('全検索', 'フィルタ検索'))
keyword = 'default(please_input_the_keyword)'
if search == 'フィルタ検索':
    keyword = st.sidebar.text_input('カンマ区切りで単語を入力してください')

def get_hour_and_minute(timestamp):
        time_parts = timestamp.split(':')
        if len(time_parts) == 3:
            hour, minute = map(int, time_parts[:2])
        else:  # MM:SS format
            hour = 0
            minute = int(time_parts[0])
        return (hour, minute)

if st.sidebar.button('実行'):
    chat = ChatDownloader().get_chat(input_url)
    df = pd.DataFrame(columns=['Timestamp', 'Author', 'Message'])
    for message in chat:
        df_tmp = pd.DataFrame([[message['time_text'], message['author']['name'], message['message']]], columns=df.columns)
        df = pd.concat([df, df_tmp], axis=0)
    df['No.'] = range(0, len(df))

    message_count = defaultdict(int)

    time_last = df[df['No.']==len(df)-1]['Timestamp'][0]
    hour_and_minute_last = get_hour_and_minute(time_last)
    hour = 0
    minute = 0
    while True:
        message_count[(hour, minute)] = 0
        if hour == hour_and_minute_last[0] and minute == hour_and_minute_last[1]:
            break
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1

    for idx in range(len(df)):
        timestamp = df[df['No.']==idx]['Timestamp'][0]
        if timestamp[0] == '-':
            continue
        if search == 'フィルタ検索':
            word_list = keyword.split(',')
            for word in word_list:
                if word in df[df['No.']==idx]['Message'][0]:
                    hour_and_minute = get_hour_and_minute(timestamp)
                    message_count[hour_and_minute] += 1
                    continue
        else:
            hour_and_minute = get_hour_and_minute(timestamp)
            message_count[hour_and_minute] += 1

    sorted_message_count = sorted(message_count.items())
    hours_and_minutes = [f"{hm[0]:02d}:{hm[1]:02d}" for hm, _ in sorted_message_count]
    counts = [count for _, count in sorted_message_count]

    fig, ax = plt.subplots()
    ax.bar(hours_and_minutes, counts)
    ax.xaxis.set_major_locator(plt.MaxNLocator(len(hours_and_minutes)//10+1))
    ax.set_xlabel('Hour:Minute')
    ax.set_ylabel('Message Count')
    ax.set_title('Message Count by Hour and Minute')
    st.pyplot(fig)