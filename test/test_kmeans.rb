require 'test/unit'
require 'lib/kmeans'
require 'lib/datafile'

class KMeansTest < Test::Unit::TestCase

  def test_it_should_cluster
    d = DataFile.make_real
    points = []
    d.samples.each do |s| 
      points << s.collect(&:to_f)
    end
    k = KMeans.new
    clusters = k.cluster(4, points)
    assert_equal clusters.size, 4
  end
  
end
