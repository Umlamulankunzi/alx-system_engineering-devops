#!/usr/bin/env ruby
input = ARGV[0]

pattern = /[A-Z]/

puts input.scan(pattern).join
