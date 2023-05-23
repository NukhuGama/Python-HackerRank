# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())

room_list = list(map(int, input().split()))
room_set = set(room_list)
# print(room_list)
# print(room_set)

# total_inroom = len(room_list)//k
# print(total_inroom)

# captain_room = 1
# for i in room_list:
#     if (room_list.count(i)==1):
#         captain_room = i
# print(captain_room)

room_sum = sum(room_list)
room_set_sum = sum(room_set) * k
captains_room = (room_set_sum - room_sum) // (k-1)
print(captains_room)





# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of  members per group where  ≠ .

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of  and the room number list.

# Input Format

# The first line consists of an integer, , the size of each group.
# The second line contains the unordered elements of the room number list.


# Constraints


# Output Format

# Output the Captain's room number.

# Sample Input

# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
# Sample Output

# 8
# Explanation

# The list of room numbers contains  elements. Since  is , there must be  groups of families. In the given list, all of the numbers repeat  times except for room number .
# Hence,  is the Captain's room number.