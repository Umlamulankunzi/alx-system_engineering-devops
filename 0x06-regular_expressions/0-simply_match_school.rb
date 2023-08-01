#!/usr/bin/env ruby
input = ARGV[0]

pattern = /School/

puts input.scan(pattern).join
