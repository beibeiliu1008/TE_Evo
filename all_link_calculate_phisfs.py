import sys
te_sfs_file = sys.argv[1]
snp_sfs_file = sys.argv[2]
newfile = f'{te_sfs_file.replace(".matched.txt","_phi_sfs.txt")}'

def get_te_sfs(te_sfs_file):
    te_dict = {}
    with open(te_sfs_file) as f:
        for line in f:
            line = line.strip('\n').split('\t')
            name = line[0]
            te_dict[name] = line[-1]
    return te_dict
te_dict = get_te_sfs(te_sfs_file)


def get_snp_sfs(snp_sfs_file):
    snp_dict = {}
    with open(snp_sfs_file) as f:
        for line in f:
            line = line.strip('\n').split('\t')
            name = line[0]
            snp_dict[name] = line[-1]
    return snp_dict
snp_dict = get_snp_sfs(snp_sfs_file)


def get_phi_sfs(newfile):
    with open(newfile,'a') as nf:
        phi_sfs_list = []
        for key in te_dict.keys():
            te_sfs = te_dict[key]
            snp_sfs = snp_dict[key]
            phi_sfs = round((float(te_sfs) - float(snp_sfs)),2)
            if phi_sfs >= 0:
                phi_sfs_list.append(phi_sfs)
            else:
                phi_sfs = 0
                phi_sfs_list.append(phi_sfs)
        phi_sfs_final = sum(phi_sfs_list)
        nf.write(f'{phi_sfs_final}\n')

get_phi_sfs(newfile)
