require 'mathn'

class Grid
  include Enumerable

  def solve
    prime_count = 0
    current_side_length = 1 
    current_max = 1
    below_10_percent = false
    layers = 0
    r = (1..3)
    while not below_10_percent
        layers += 1
	r.each do |num|
	  diagonal_number = current_side_length**2 + num * (1 + current_side_length)
          prime_count += 1 if diagonal_number.prime?
        end
        current_side_length += 2

	ratio = prime_count.to_f / (2.0*current_side_length - 1)
	if (layers % 100 == 0)
	  p ratio
	end	
        if ratio < 0.1
	  below_10_percent = true
        end
    end
    return current_side_length
  end

end


grid = Grid.new
p grid.solve