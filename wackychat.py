"""
CSCA08: Winter 2024 -- Assignment 3: WackyChat

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

from copy import deepcopy
from typing import TextIO
from datetime import datetime
import tempfile
import os

# This is an example of what the contents of a file might look like.
SAMPLE_TEXT_CONTEXT_1 = """
GROUP
9119
CSCA08
CHANNEL
48805
9119
Irene's Classroom
CHANNEL
6265
9119
Purva's Classroom
MESSAGE
12255
48805
2024/11/16 23:32:52
Charles Xu
I am working on CSCA08 Assignment 3!
DONE
"""


# This is the translation of the above contents as a series of dicts & arrays.
SAMPLE_DICT_CONTEXT_1 = {
    "groups": [{
        "id": 9119,
        "name": "CSCA08"
    }],
    "channels": [{
        "id": 48805,
        "group": 9119,
        "name": "Irene's Classroom"
    }, {
        "id": 6265,
        "group": 9119,
        "name": "Purva's Classroom"
    }],
    "messages": [{
        "id": 12255,
        "channel": 48805,
        "time": "2024/11/16 23:32:52",
        "name": "Charles Xu",
        "message": "I am working on CSCA08 Assignment 3!"
    }]
}

SAMPLE_DICT_CONTEXT_2 = {
    "groups": [{
        "id": 9119,
        "name": "CSCA08"
    }],
    "channels": [{
        "id": 6265,
        "group": 9119,
        "name": "Purva's Classroom"
    }, {
        "id": 48805,
        "group": 9119,
        "name": "Irene's Classroom"
    }],
    "messages": [{
        "id": 12255,
        "channel": 48805,
        "time": "2024/11/16 23:32:52",
        "name": "Charles Xu",
        "message": "I am working on CSCA08 Assignment 3!"
    }]
}

def is_valid_date(date: str) -> bool:
    '''
    Returns True if and only if the given string 'date' is valid and in the
    format of 'year/month/day hour:minute:second'.

    >>> is_valid_date('2024/11/16 23:32:52')
    True
    >>> is_valid_date('2024/13/13 25:25:25')
    False
    >>> is_valid_date('Banana')
    False
    '''
    try:
        datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
        return True
    except ValueError:
        return False


def create_temporary_file() -> str:
    '''
    Create a temporary file inside the system's temporary directory and return
    its absolute path.

    >>> file_path = create_temporary_file()
    >>> os.path.exists(file_path)
    True
    >>> os.remove(file_path)
    >>> os.path.exists(file_path)
    False
    '''
    return tempfile.NamedTemporaryFile(delete=False).name

def is_item_in_context(context:dict, iid: int, kind: str) -> bool:
    '''Return True iff an item of kind with iid exists in context.

    >>> is_item_in_context(SAMPLE_DICT_CONTEXT_1, 9119, 'groups')
    True
    >>> is_item_in_context(SAMPLE_DICT_CONTEXT_1, 1111, 'messages')
    False
    '''
    id_list = []
    if kind in context:
        for item in context[kind]:
            id_list.append(item['id'])
        if iid in id_list:
            return True
    return False

def list_equal(list1: list, list2:list) -> bool:
    '''Return whether or not two lists have the same content, regardless of
    order.

    >>> list_equal([1,2,3,4], [4,2,3,1])
    True
    '''
    ret = False
    if len(list1) == len(list2):
        ret = True
        for item in list1:
            if item not in list2:
                ret = False
    return ret

def sanitize_context_array(context: dict, key: str) -> None:
    '''Modify the key of the given context so that key has a default value empty
    list and lists with same contents are same.

    Precondition: key is one of 'groups', 'channels', 'messages'

    >>> dic = {'groups': [{'id': 2, 'name': '2'}, {'id':1, 'name': '1'}]}
    >>> sanitize_context_array(dic, 'groups')
    >>> dic == {'groups': [{'id':1, 'name': '1'}, {'id': 2, 'name': '2'}]}
    True
    '''
    if key not in context:
        context[key] = []
    else:
        context[key] = sorted(context[key], key=lambda x: x.get('id', 0))


def context_equals(context1: dict, context2: dict) -> bool:
    '''Evaluate if two contexts are equal regardless of the ordering of lists.

    >>> context_equals(SAMPLE_DICT_CONTEXT_1, SAMPLE_DICT_CONTEXT_2)
    True
    '''
    for key in ['groups', 'channels', 'messages']:
        sanitize_context_array(context1, key)
        sanitize_context_array(context2, key)
    return context1 == context2



def create_group(context: dict, group_id: int, name: str) -> bool:
    '''
    Create a new group in context with group id group_id and name name only when
    the group id does not already exist. Return True if the action is
    successful, False otherwise.

    >>> dic = {'channels': []}
    >>> create_group(dic ,11910, 'strbry')
    True
    >>> dic == {'groups': [{'id': 11910, 'name': 'strbry'}], 'channels': []}
    True
    '''
    id_list = []
    ret = False
    if "groups" not in context:
        context["groups"] = [{"id":group_id, "name": name}]
        ret = True
    else:
        for group in context['groups']:
            id_list.append(group['id'])
        if group_id not in id_list:
            context["groups"].append({"id":group_id, "name": name})
            ret = True
    return ret


def create_channel(context: dict, group_id: int, channel_id: int,
                   name: str) -> bool:
    '''
    Create a new channel with a channel id channel_id and name name that belongs
    to the group_id group in context. This is successful only when no other
    channel with channel_id exist and the group exists in context. Return True
    if the action is successful, False otherwise.

    >>> dic = {'channels': [{"id": 27, 'name': '27', 'group': 166}], \
'groups': [{'id': 166, 'name':'166'}]}
    >>> create_channel(dic, 166, 28, '28num')
    True
    >>> context_equals(dic, {'channels': [{"id": 27, 'name': '27', 'group': \
166}, {"id": 28, 'name': '28num', 'group': 166}], 'groups': [{'id': 166, \
'name':'166'}]})
    True
    '''
    ret = False
    if is_item_in_context(context, group_id, 'groups'):
        id_list = []
        if "channels" not in context:
            dic = {"id":channel_id, "name": name, 'group': group_id}
            context["channels"] = [dic]
            ret = True
        else:
            for channel in context['channels']:
                id_list.append(channel['id'])
                if channel_id not in id_list:
                    context["channels"].append({"id":channel_id, "name": name,
                                                'group': group_id})
                    ret = True
    return ret


def send_message(context: dict, channel_id: int, message_id: int,
                 time: str, name: str, message: str) -> bool:
    '''
    Create a new message with its id message_id, its time time, and its author
    name, its content message, and the channel_id channel it was created in.
    This is successful only when no other message with message_id exist and the
    channel exists in context. Return True if the action is successful, False
    otherwise.

    >>> dic = {'channels': [{'id': 110, 'name': 'a', 'group': 110}]}
    >>> send_message(dic, 110, 110, '2024/1/16 20:32:52', 'aut', 'aaaa')
    True
    >>> context_equals(dic,  {'channels': [{'id': 110, 'name': 'a', 'group': \
    110}], 'messages': [{'id': 110, 'name': 'aut', 'message': 'aaaa', 'time': \
    '2024/1/16 20:32:52', 'channel': 110}]})
    True
    '''
    ret = False
    dic = {"id":message_id, "name": name, 'channel':channel_id, 'time': time,
           'message': message}
    if is_valid_date(time):
        if is_item_in_context(context, channel_id, 'channels'):
            id_list = []
            if "messages" not in context:
                context["messages"] = [dic]
                ret = True
            else:
                for mes in context['messages']:
                    id_list.append(mes['id'])
                    if message_id not in id_list:
                        context["messages"].append(dic)
                        ret = True
    return ret


def read_context_from_file(file_io: TextIO) -> dict | None:
    '''
    Return a new context by reading the contents of the given opened file
    file_io. Return None if the action wasn't successful.

    Preconditions: file_io has been opened for reading.
    file_io follows the format GROUP/CHANNEL/MESSAGE + information.
    file_io contains at least one DONE

    >>> file_path = create_temporary_file()
    >>> file = open(file_path, "w")
    >>> index = file.write(SAMPLE_TEXT_CONTEXT_1)
    >>> file.close()
    >>> file = open(file_path, "r")
    >>> context = read_context_from_file(file)
    >>> file.close()
    >>> context_equals(context, SAMPLE_DICT_CONTEXT_1)
    True
    '''
    context = {}
    ret = False
    lines = file_io.readlines()
    if 'DONE\n' in lines:
        lines = lines[:lines.index('DONE\n')]
    else:
        lines = lines[:lines.index('DONE')]
    sublist = deepcopy(lines)
    while 'GROUP\n' in sublist:
        group_id = int(sublist[sublist.index('GROUP\n') + 1][:-1])
        name = sublist[sublist.index('GROUP\n') + 2][:-1]
        if not create_group(context, group_id, name):
            ret = True
        sublist = sublist[sublist.index('GROUP\n') + 3:]
    sublist = deepcopy(lines)
    while 'CHANNEL\n' in sublist:
        channel_id = int(sublist[sublist.index('CHANNEL\n') + 1][:-1])
        group_id = int(sublist[sublist.index('CHANNEL\n') + 2][:-1])
        name = sublist[sublist.index('CHANNEL\n') + 3][:-1]
        if not create_channel(context, group_id, channel_id, name):
            ret = True
        sublist = sublist[sublist.index('CHANNEL\n') + 4:]
    sublist = deepcopy(lines)
    while 'MESSAGE\n' in sublist:
        message_id = int(sublist[sublist.index('MESSAGE\n') + 1][:-1])
        channel_id = int(sublist[sublist.index('MESSAGE\n') + 2][:-1])
        time = sublist[sublist.index('MESSAGE\n') + 3][:-1]
        author = sublist[sublist.index('MESSAGE\n') + 4][:-1]
        content = sublist[sublist.index('MESSAGE\n') + 5][:-1]
        if not send_message(context, channel_id, message_id, time, author, \
                            content):
            ret = True
        sublist = sublist[sublist.index('MESSAGE\n') + 6:]
    if ret:
        return None
    return context


def get_user_word_frequency(context: dict, name: str) -> dict:
    '''
    Return a dictionary that maps every word in messages of name in context
    to its used frequency. A word is defined as a series of characters in a
    sentence, split up by spaces.

    >>> context = {'messages': [{'name': 'Charles', 'message': 'Hello world'},\
{'name': 'Charles', 'message': 'Hello again. world.'}]}
    >>> get_user_word_frequency(context, 'Charles')
    {'Hello': 2, 'world': 1, 'again.': 1, 'world.': 1}
    '''
    freq = {}
    words = []
    for a_message in context['messages']:
        if a_message['name'] == name:
            words += a_message['message'].split(' ')
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    return freq


def get_user_character_frequency_percentage(context: dict, name: str) -> dict:
    '''
    Return a dictionary that maps every character in messages of name in context
    to its used frequency percentage.

    >>> get_user_character_frequency_percentage(SAMPLE_DICT_CONTEXT_1, 'Charles\
 Xu')
    {'I': 0.027777777777777776, ' ': 0.16666666666666666, 'a': 0.02777777777777\
7776, 'm': 0.05555555555555555, 'w': 0.027777777777777776, 'o': 0.055555555\
55555555, 'r': 0.027777777777777776, 'k': 0.027777777777777776, 'i': \
0.05555555555555555, 'n': 0.1111111111111111, 'g': 0.05555555555555555, \
'C': 0.05555555555555555, 'S': 0.027777777777777776, \
'A': 0.05555555555555555, '0': 0.027777777777777776, \
'8': 0.027777777777777776, 's': 0.05555555555555555, \
'e': 0.027777777777777776, 't': 0.027777777777777776, \
'3': 0.027777777777777776, '!': 0.027777777777777776}
    '''
    freq = {}
    chars = ''
    for a_message in context['messages']:
        if a_message['name'] == name:
            chars += a_message['message']
    for char in chars:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    num = sum(freq.values())
    for char in freq:
        freq[char] /= num
    return freq



def get_most_popular_group(context: dict) -> int | None:
    '''
    Return the group id of the most popular group in context. The most popular
    group is defined as the group that sends the most amount of messages.
    Return None if no groups exist in context.
    If multiple groups are tied, return the smallest id.

    >>> context = {'groups': [{'id': 111, 'name':'a'}, {'id': 222, 'name':\
2}], 'channels': [{'group': 111, 'name': 'ac', 'id': 111}, {'group':111,\
'name': 'bc', 'id': 222}], 'messages': [{"id": 12255, "channel": 111, "time": \
"2024/11/16 23:32:52", "name": "Charles Xu", "message": "I am working on \
CSCA08 Assignment 3!"}, {"id": 12345,"channel": 111,"time": "2024/11/16 \
23:32:52","name": "Charles Xu","message": "I am working on CSCA08 Assignment \
3!"}, {"id": 1234,"channel": 222,"time": "2024/11/16 23:32:52","name": "Charles\
 Xu","message": "I am working on CSCA08 Assignment 3!"}]}
    >>> get_most_popular_group(context)
    111
    >>> context = {'groups': [{'id': 111, 'name':'a'}, {'id': 10, 'name':\
2}], 'channels': [{'group': 111, 'name': 'ac', 'id': 111}, {'group':10,\
'name': 'bc', 'id': 222}], 'messages': [{"id": 12255, "channel": 111, "time": \
"2024/11/16 23:32:52", "name": "Charles Xu", "message": "I am working on \
CSCA08 Assignment 3!"}, {"id": 1234,"channel": 222,"time": "2024/11/16 \
23:32:52","name": "Charles\
 Xu","message": "I am working on CSCA08 Assignment 3!"}]}
    >>> get_most_popular_group(context)
    10
    '''
    g_dic = {}
    for group in context['groups']:
        g_dic[group['id']] = [[], 0]
    for channel in context['channels']:
        if channel['group'] in g_dic:
            g_dic[channel['group']][0] += [channel['id']]
    for message in context['messages']:
        for group_id, arr in g_dic.items():
            if message['channel'] in arr[0]:
                arr[1] +=1
    if len(g_dic) == 0:
        return None
    num = 0
    max_mess = 0
    for group_id, arr in g_dic.items():
        if arr[1] > max_mess:
            num = group_id
            max_mess = arr[1]
        elif arr[1] == max_mess:
            num = min(num, group_id)
    return num


if __name__ == '__main__':
    import doctest
    doctest.testmod()
