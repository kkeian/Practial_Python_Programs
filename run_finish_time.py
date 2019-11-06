#! python3
#   Copyright (C) 2019 Keian Kaserman 

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import re

# use this to pick out the hour or minute or second
find_time = re.compile(r'([0-23]):([0-59])')

has_decimal = re.compile(r'\.')

print('Enter run start time (format hh:mm): ', end=' ')
start_time = input()

while not find_time.search(start_time):
    print('Enter run start time (format hh:mm): ', end=' ')
    start_time = input()
  
# Allows mathematical operations on entered start time
#  IOT calculate finish time.
hour_start = int(find_time.search(start_time).group(1))
minute_start = int(find_time.search(start_time).group(2))

print('What is your "easy pace"? (format mm:ss)', end=' ')
e_pace = input()
print('How many miles will you run at this pace? ', end=' ')
easy_miles = int(input())

# Allows mathematical operations on entered easy pace
e_min_per_mile = int(find_time.search(e_pace).group(1))
e_sec_per_mile = int(find_time.search(e_pace).group(2))

print('What is your "tough pace"? (format mm:ss)', end=' ')
t_pace = input()
print('How many miles will you run at this pace? ', end=' ')
tough_miles = int(input())

# Allows mathematical operations on entered hard pace
t_min_per_mile = int(find_time.search(t_pace).group(1))
t_sec_per_mile = int(find_time.search(t_pace).group(2))

print('What is your "cooldown pace"? (format mm:ss)', end=' ')
c_pace = input()
print('How many miles will you walk at this pace? ', end=' ')
cooldown_miles = input()
if has_decimal.search(cooldown_miles):
    cooldown_miles = float(cooldown_miles)
else:
    cooldown_miles = int(cooldown_miles)

# Allows mathematical operations on entered cooldown pace
c_min_per_mile = int(find_time.search(c_pace).group(1))
c_sec_per_mile = int(find_time.search(c_pace).group(2))

# hours to seconds converter
# usage: * hours_seconds to convert hours
#   // by hours_seconds to convert seconds
hours_seconds = 60 ** 2

# minutes to seconds converter
# usage: * minutes_seconds to convert minutes
#   // by minutes_seconds to convert seconds
minutes_seconds = 60

start_time = (hour_start * hours_seconds + (minute_start * minutes_seconds))

# creates variable to multiply later by number of miles
#  ran at easy_pace.
easy_pace = e_min_per_mile * minutes_seconds + e_sec_per_mile

# creates variable to multiply later by number of miles
#  ran at tough_pace
tough_pace = (t_min_per_mile * minutes_seconds + t_sec_per_mile)
# creates variable to add to end of run for cooldown time
cooldown_pace = (c_min_per_mile * minutes_seconds + c_sec_per_mile)

finish_time_secsince_midnight = (start_time + (easy_pace * easy_miles) +
                                 (tough_pace * tough_miles) + (cooldown_pace *
                                                               cooldown_miles))

finish_time_secsince_midnight = int(finish_time_secsince_midnight)
arrival_home_hour = (finish_time_secsince_midnight // hours_seconds)
arrival_home_minute = round((((finish_time_secsince_midnight % hours_seconds) //
              minutes_seconds) * minutes_seconds), 2)
s_two_digit_time = slice(2)
arrival_home_minute = (str(arrival_home_minute)[s_two_digit_time])

arrival_time = (str(arrival_home_hour) + ':' + arrival_home_minute)
print('Return time - ' + arrival_time)
