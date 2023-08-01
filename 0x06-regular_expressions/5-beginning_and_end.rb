#!/usr/bin/env ruby
input = ARGV[0]

pattern = /h.n/

puts input.scan(pattern).join
