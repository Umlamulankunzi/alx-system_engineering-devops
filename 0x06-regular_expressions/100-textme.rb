#!/usr/bin/env ruby
input = ARGV[0]

pattern = /\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/

puts input.scan(pattern).join(',')

