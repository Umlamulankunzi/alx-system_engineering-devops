#!/usr/bin/env ruby
input = ARGV[0]

pattern = /\A\d{10}\z/

puts input.scan(pattern).join
