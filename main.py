def count_batteries_by_usage(cycles):
    low_count=0
    mid_count=0
    high_count=0
    counts=dict()
    for x in cycles:
        if x<=400:
            low_count+=1
        elif x>400 and x<=919:
            mid_count+=1
        else:
            high_count+=1
    counts['lowCount']=low_count
    counts['mediumCount']=mid_count
    counts['highCount']=high_count
            
    return counts


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  print('lowCount:',counts['lowCount'])
  print('mediumCount',counts['mediumCount'])
  print('highCount:',counts['highCount'])
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
