#!/usr/bin/env ruby
input = ARGV[0]

pattern = /hbt{2,5}n/

puts input.scan(pattern).join
