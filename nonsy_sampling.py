#this sampling is based on Jeff's suggestion


import sys
#import numpy as np
import pandas as pd
import numpy as np
nonsyn_file = sys.argv[1]
binned_file = f'{nonsyn_file.replace(".txt","_bins.txt")}'
syn_file = sys.argv[2]
# output_file = f'{syn_file.split(".")[0]}_sampling_rep1.txt'
output_file = sys.argv[3]

def get_each_bin_line_number_in_nonsy(nonsyn_file):
    with open(nonsyn_file) as f:
        #next(f)
        number_lines = len(f.readlines())
        # print(number_lines)
        each_bin_lines = number_lines//10 + 1
        return each_bin_lines

each_bin_lines = get_each_bin_line_number_in_nonsy(nonsyn_file)

def get_binnedfile_nonsysn(nonsyn_file):
    with open(nonsyn_file) as f:
        with open(binned_file,'w') as nf:
            #next(f)
            count = 0
            for line in f:
                count += 1
                line = line.strip('\n').split('\t')
                bin = count//each_bin_lines + 1
                newline = '\t'.join(line)
                nf.write(f'{newline}\t{bin}\n')

get_binnedfile_nonsysn(nonsyn_file)

def get_ages_for_each_bin(binned_file):
    bin_age = {}
    with open(binned_file) as f:
        for line in f:
            line = line.strip('\n').split('\t')
            bin_name = line[-1]
            age = line[1]
            bin_age.setdefault(bin_name,[]).append(float(age))
    return bin_age

bin_age = get_ages_for_each_bin(binned_file)


def get_age_bounday_for_each_bin():
    bin_boundary = {}
    for bin_name in bin_age.keys():
        age_range = bin_age[bin_name]
        age_boundary = []
        min_age = min(age_range)
        age_boundary.append(min_age)
        max_age = max(age_range)
        age_boundary.append(max_age)
        length = len(age_range)
        age_boundary.append(length)
        bin_boundary[bin_name] = age_boundary
    return bin_boundary

bin_boundary = get_age_bounday_for_each_bin()



def get_sampled_syn_snp(syn_file):
    with open(output_file,'w') as nf:
        for bin in bin_boundary.keys():
            # print(bin)
            min_age = float(bin_boundary[bin][0])
            # print(min_age)
            max_age = float(bin_boundary[bin][1])
            # print(max_age)
            length = int(bin_boundary[bin][2])
            # print(length)
            sys_snps = []
            with open(syn_file) as f:
                #next(f)
                for line in f:
                    line = line.strip('\n').split('\t')
                    # print(line)
                    if min_age <= float(line[1]) <= max_age:
                        newline = '\t'.join(line[:])
                        final_line = f'{newline}\t{bin}'
                        sys_snps.append(final_line)
                # print(len(sys_snps))
                # print(sys_snps)
            random_sys_snps = np.random.choice(sys_snps,length,replace=True)
            for i in random_sys_snps:
                nf.write(f'{i}\n')

get_sampled_syn_snp(syn_file)
 

