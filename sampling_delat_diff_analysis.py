#the following is to calculate the delta diff
import sys
import statistics
nonsyn_file = sys.argv[1]
syn_sampling_file = sys.argv[2]
#output_file = f'nonsyn_syn_delta_diff_{syn_sampling_file.split("_")[-1]}'
output_file = sys.argv[3]


def get_nonsyn_bin_sfs(nonsyn_file):
    nonsyn_bin_sfs = {}
    bin_age = {}
    with open(nonsyn_file) as f:
        for line in f:
            line = line.strip('\n').split('\t')
            bin_name = line[-1]
            nonsyn_bin_sfs.setdefault(bin_name,[]).append(float(line[-2]))
            bin_age.setdefault(bin_name,[]).append(float(line[1]))
    return (nonsyn_bin_sfs, bin_age)

nonsyn_bin_sfs, bin_age = get_nonsyn_bin_sfs(nonsyn_file)


def get_syn_bin_sfs(syn_sampling_file):
    syn_bin_sfs = {}
    with open(syn_sampling_file) as f:
        for line in f:
            line = line.strip('\n').split('\t')
            bin_name = line[-1]
            syn_bin_sfs.setdefault(bin_name,[]).append(float(line[-2]))
    return syn_bin_sfs

syn_bin_sfs = get_syn_bin_sfs(syn_sampling_file)




def get_syn_nonsy_delta_diff():
    with open(output_file,'w') as f:
        for key in nonsyn_bin_sfs.keys():
            # print(key)
            med_age = statistics.median(bin_age[key])
            avg_sfs_nonsyn = round(sum(nonsyn_bin_sfs[key])/len(nonsyn_bin_sfs[key]),2)
            # print(avg_sfs_nonsyn)
            avg_sfs_syn = round(sum(syn_bin_sfs[key])/len(syn_bin_sfs[key]),2)
            # print(avg_sfs_syn)
            delta_diff = round(avg_sfs_nonsyn - avg_sfs_syn, 2)
            # print(delta_diff)
            f.write(f'{key}\t{delta_diff}\t{med_age}\n')

get_syn_nonsy_delta_diff()
