# Ruby Cheat Sheet

=begin
This is also an example of a multi-line comment
=end


#################
## Basic Stuff ##
#################

# In terminal, 'irb' starts interactive ruby



########################
## Naming Conventions ##
########################

# Variables should be snake_case

# Constants should be UPPER_CASE

# Methods should be snake_case







##################
## I/O Commands ##
##################

# Print to screen with print or puts / p (with \n)
print 'hello'     # => 'hello'
puts 'hello'      # => 'hello'
p 'hello'         # => 'hello'

# Get user input with gets
name = gets       # => input/n

# Trim /n with the .chomp function
name = gets.chomp # => input












######################
## Basic Data Types ##
######################

### Numbers ###

# Division with integers results in an integer
17 / 5  # => is 3, not 3.4
17 / 5.0  # => 3.4

# % is a modulo


# Converting Number Types

# .to_f and .to_i convers int to float and vice versa
13.to_f   # => 13.0
13.0.to_i   # => 13


# Useful numeric methods

# .even? and .odd? return eveness/oddness of a value. No need to % 2 == 0!
6.even? #=> true
7.odd? #=> true






### Strings ###

# Strings are mutable in Ruby! Wow!

# Strings can be defined with 'single' or "double" quotes, like python(3)
"The man said, 'Hi there!'"     # => The man said, 'Hi there!'
'The man said, \' Hi there!\''  # => The man said, 'Hi there!'

# Converting to a String with .to_s
5.to_s  #=> "5"

# Concatenation

# plus (+), shovel (<<), and concat method (.concat()) all work
# + is slow because it creates a new string, whereas shovel or concat mutate the original
"this " + "is " + "a " + "string."
"this " << "is " << "also " + "a string."
"this ".concat("works ").concat("as well.")

# Interpolation
# This ONLY works with "double quotes"!
name = "Eric"
"My name is #{name}"


# Substrings
"hello"[0]    # => "h"
"hello"[0..1] # => "he"
"hello"[0..4] # => "hell"
"hello"[-1]   # => "o"

# Escape characters
\\  #=> Need a backslash in your string?
\b  #=> Backspace
\r  #=> Carriage return, for those of you that love typewriters
\n  #=> Newline. You'll likely use this one the most.
\s  #=> Space
\t  #=> Tab
\" "#=> Double quotation mark
\' '#=> Single quotation mark


# Other common and useful string methods
"hello".capitalize      # => "Hello"
"hello".include?("lo")  # => true
"hello".upcase          # => "HELLO"
"Hello".downcase        # => "hello"
"hello".empty?          # => false
"hello".length          # => 5
"hello".reverse         # => "olleh"
"hello world".split     # => ["hello", "world"]
"hello".split("")       # => ["h", "e", "l", "l", "o"]
"hello      ".strip     # => "hello"
"hello".each_char       # enumerates each character

# #ord converts alpha character to numeric value:
'a'.ord  # => 94

# #chr converts numeric value to alpha character
94.chr   # => 'a'





### Symbols ###

# Declare a symbol like this:
:my_symbol
:"string_symbol"

# Symbols are (kinda) non-mutable strings. Two symbols with the same name are the same symbol
"string" == "string"                      # => true
"string".object_id == "string".object_id  # => false
:symbol.object_id == :symbol.object_id    # => true


### Booleans ###

# They're booleans. Lowercase, you dirty pythonista
true
false




### Nothing ###

# the nothing value is denotated with 'nil', like None or null
nil

# To perform a null (or nil) check, add a '?'
"Hello, world".nil?   # => false












############
## Arrays ##
############
# https://ruby-doc.org/core-2.6/Array.html

# Arrays are mutable

# There are multiple ways of creating arrays. Thanks Ruby
empty_array = []        # creates an empty array
new_array = [1, 2, 3]   # creates array with some elements

# When creating a string array, this is an alternative:
strings = %w[hello world]  # => ['hello', 'world']

# The Array.new method creates arrays with optional arguments:
Array.new               # => []
Array.new(3)            # => [nil, nil, nil]
Array.new(3, 'Hello')   # => ['Hello', 'Hello', 'Hello']
Array.new(3, Array.new) # => [[], [], []]

# Accessing arrays is standard. Negative indicies return elements from the end
new_array[2] = 4        # array is now [1, 4, 3]
new_array[-1]           # => 3

# #first and #last return the first or last n elements
new_array.first       # => 1
new_array.first(2)    # => [1, 2]
new_array.last(2)     # => [2, 3]


## Adding elements to an array
# shovel (<<) and #push both append elements to the end, but shovel is better for adding a single element
numbers = [1, 2]
numbers.push(3, 4)
numbers << 5

# #unshift adds elements to the beginning and returns the mutated array
numbers.unshift(0)  # => [0, 1, 2, 3, 4, 5]


## Remove elements from an array
# #pop removes the element at the end of an array and returns it
numbers.pop   # => 5, and the array is now [0, 1, 2, 3, 4]

# #shift removes the element at the front of an array
numbers.shift # => 0, and the end array is now [1, 2, 3, 4]

# #delete_at removes the element at the specified location:
numbers.delete_at(1)


## Iterating over array
# #each enumerates over VALUES in the array
array.each { |item| puts item }   # => prints each item in the array

# the longer do...end format is:
array.each do |item|
    puts item
end

# #each_with_index enumerates values AND indicies
array.each_with_index { |item, index| puts '#{item} #{index}' }

# #map (or #collect) returns a new array with a method applies to all elements
# #map! (bang) modifies the array in-place
users = users.map { |user| user.capitalize}
users = users.map(&:capitalize)
users.map!(&:capitalize)

# #select (or #filter) filters the array based on provided criteria
numbers = [3, 4, 12, 2, 49]
numbers.select { |n| n > 10 }   # => returns [12, 49]

# #reject filters the array by excluding matches
numbers.reject { |n| n < 4}     # => returns [4, 12, 49]

# #reduce (or #inject) returns an array to single value
my_numbers = [5, 6, 7, 8]
sum = 0
my_numbers.each { |number| sum += number }

# ^^ above could be replaced with the following below:
my_numbers.reduce { |sum, number| sum + number}


# Some other useful array methods:
array = [1,2,3]
array.empty?      # => false
array.length      # => 3
array.reverse     # => [3, 2, 1]
array.include?(3) # => true
array.join        # => '123'
array.join(' ')   # => '1 2 3'
array.sort













############
## Hashes ##
############
# https://ruby-doc.org/core-2.6/Hash.html

# Create a new hash (dictionary, hash map, hash table, etc.) with {} or Hash.new
empty_hash = {}
another_empty_hash = Hash.new
new_hash = {
  'key1' => 'value1',
  'key2' => 'value2',
  3 => 1321234
}

# Access a value with hash[key]
puts my_hash['key']   # => puts value pair of key

# Keys may also be a :symbol
# When instantiating a hash with symbols, it looks like this:
symbol_hash = {
  key1: 'value1',
  key2: 'value2'
}

# and getting accessing an entry looks like this:
symbol_hash[:key1]  # Will return nil if :key1 is not found

# #fetch returns a value as well, but will raise a KeyError is the key is not found.
symbol_hash.fetch(:key3)  # => KeyError: key not found: :key3
symbol_hash.fetch(:key3, 'a value')   # => 'a value'


# #delete removes a key-value pair and returns it
symbol_hash.delete(:key1)

# the #keys and #values methods return arrays of they keys and values in a hash
symbol_hash.keys      # => [:key1, :key2]
symbol_hash.values    # => ['value1', 'value2']

# #merge combines two hashes. hash2 will override hash1 keys if any overlap

# When use the #each enumerable in hashes, elements can be retrieved as |key, value| or |pair|, a pair is an array of [key, value]
my_hash = { one: 1, two: 2 }
my_hash.each { |key, value| puts '#{key} #{value}'}
my_hash.each { |pair| puts '#{pair}'}







###########
## Scope ##
###########

# Global variables are declared with '$'
$global_var = 'available through the app'

# Class variables are declared with '@@'
@@class_var = 'accessible by instances of class, as well as the class itself'

# Instance variables are declared with '@'
@instance_var = 'available throughout current instance of class'

# Local variables do not have any designation
local_variable = 'cannot cross scope boundaries'









##################
## Conditionals ##
##################

# Unlike other languages, Ruby only evaluates false and nil as falsey. Everything else is truthy
false # is false
nil # is false
true # is true
"" # is true
0 # is true

# if statements look like this:
if something == true
  # something happens here
elsif something == false
  # something else happens here
else
  # otherwise do this
end

# end is not necessary if the conditional is on one line
puts 'this is one line' if 1 < 2


# == compares equality of values
1 == 1 # true
1 == 2 # false

# != compares inequality of values
1 != 1 # false
1 == 2 # true

# >, <, >=, <= works like normal


# eql? checks value AND type
5.eql?(5)     # => true
5.eql?(5.0)   # => false because int != float

# equal? checks if values are the same object in memory
"string".equal?("string")   # => false

# The spaceship operator ( <==> ) returns:
#   -1 if the value on the left is less than the value on the right
#   0 if the value on the left is equal to that on the right
#   1 if the value on the left is greater than the value on the right
# This is most commonly used in sorting functions
5 <==> 10   # => -1
10 <==> 10  # => 0
10 <==> 5   # => 1


## Logical operators
# &&, ||, and ! are and, or, and not, respectively

# Ruby complies with short circuit evaluation, which means:
# With && and ||, if the first argument fails (or passes), the second 

# && and || can be written as 'and' and 'or', respectively


## Case Statements
grade = 'F'
did_i_pass = case grade
  when 'A' then 'Yes'
  when 'D' then 'No'
  else 'Maybe'
end


# The 'then' keyword is useful when using a case to assign a simple value
# For something more complex, forgo the 'thens'

grade = 'F'
case grade
when 'A'
  puts "You're a genius"
  future_bank_account_balance += 5,000,000
when 'D'
  puts "Better luck next time"
  can_i_retire_soon = false
else
  puts "McDonald's is hiring!"
  fml = true
end


## Unless Statement
# Unless statements are inverted if statements, making it more readable than if !true
this_is_true = true
unless this_is_true
  puts 'this is false'
end


## Ternary Operator
# condition statement ? <execute if true> : <execute if false>






###########
## Loops ##
###########

## Loop
# Loop runs indefinitely until a break is called
i = 0
loop do
  i += 1
  break if i == 10
end


## While loop
i = 0
while i < 10 do
  i += 1
end

while gets.chomp != 'yes' do
  puts 'Will you go to prom with me?'
end


## Until loop
# Unlike a while loop, Until loops as long as the input is false
i = 0
until i > 10 do
  i += 1
end


## For loop
# For loops depend on the Range function:
(1..5)    # inclusive range: 1, 2, 3, 4, 5
(1...5)   # exclusive range: 1, 2, 3, 4

for i in 0..5
  puts i
end


## Times loop
# A specific for loop that starts at 0 and loops n.times
5.times do
  puts 'i will do this 5 times'
end

# The iteration can be used by including |number|
5.times do |number|
  puts 'this is number #{nunber}'
end


## Upto and Downto loops
# Another counting loop with a slight shorthand
5.upto(10) { |num| print "#{num} " }    # => 5 6 7 8 9 10
10.downto(5) { |num| print "#{num}"}    # => 10 9 8 7 6 5









#############
## Methods ##
#############

# Method names can end in ?, !, and =
# Reserved words: http://www.java2s.com/Code/Ruby/Language-Basics/Rubysreservedwords.htm

def method_name(arguments = 'defailt parameters')
  #do something
  new_thing = arguments
  return new_thing
end

# Ruby allows implicit returns, but stick with explicit

## Predicate Methods
# Predicates end with ? and are a naming convention indicating that a boolean is returned

## Bang Methods
# Bangs end with ! and are a naming convention indicating that the object will be mutated vs. returning a modified copy







########################
## Debugging with Pry ##
########################
# https://learn.co/lessons/debugging-with-pry

# Aftering installing the pry gem, bindings allow breakpoints
require 'pry'

# do something
binding.pry

# Pry REPL will allow debugging of variables