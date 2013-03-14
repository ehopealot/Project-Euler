
def is_english(potential_plaintext)
  #rough and dirty way to figure out if the text has 'common english words'
  potential_plaintext.index(' to ') and potential_plaintext.index(' and ')
end


def solve
  File.open("cipher1.txt") do |file|
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = []
    file.each do |row|
      encrypted_text.concat row.chomp.split(',').map {|x| x.to_i}
    end
    p encrypted_text
    alphabet.each_byte do |char1|
      alphabet.each_byte do |char2|
        alphabet.each_byte do |char3|
          potential_key = [char1, char2, char3]
          key_idx = 0
	  potential_plaintext = ""
	  ascii_sum = 0
          encrypted_text.each do |ascii_val|
            ascii_val = (potential_key[key_idx%3]^ascii_val)
	    potential_plaintext = potential_plaintext + ascii_val.chr
	    ascii_sum += ascii_val
 	    key_idx += 1       
          end
	  if is_english potential_plaintext
	     p ascii_sum
             return potential_plaintext
          end
        end
      end
    end
  end
end


p solve