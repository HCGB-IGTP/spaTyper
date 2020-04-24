#!/usr/bin/env python3

import sys
import string
from itertools import groupby

""" 
This script contains several useful functions employed along the spa_typing code.
"""

####################################################
def revseq(seq):
    """
    Reverse translate the sequence.
     
    .. attention:: Be aware of Copyright

        The code implemented here was retrieved and modified from spa_typing (https://github.com/mjsull/spa_typing)
    
        Give him credit accordingly.  
    """
    transtab = string.maketrans('atcgATCG', 'tagcTAGC')
    seq = seq[::-1]
    seq = seq.translate(transtab)
    return seq

####################################################
def fasta_dict(fasta_name):
    """
    Create dictionary from fasta file.
    
    Given a fasta file. yields a dict of header, sequence
    
    .. attention:: Be aware of Copyright

        The code implemented here was retrieved and modified from spa_typing (https://github.com/mjsull/spa_typing)
    
        Give him credit accordingly.  
    
    """
    seqDict = {}
    with open(fasta_name) as fh:
        faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
        for header in faiter:
            header = header.__next__()[1:].strip()
            seq = "".join(s.strip() for s in faiter.__next__())
            if header in seqDict:
                sys.exit('FASTA contains multiple entries with the same name')
            else:
                seqDict[header] = seq
    return seqDict

####################################################
def download_file_repeats(folder):
    """
    Downloads spa types file from SeqNet/Ridom Spa Server.
    
    Given a folder absolute path ``folder``, it initially checks if file :file:`sparepeats.fasta` is
    available. It checks for a timestamp previosuly generated and returns if it is available. If file
    is not accessible it tries to download it from url site: http://spa.ridom.de/dynamic/sparepeats.fasta
    
    :param folder: Absolute path to folder containing SeqNet/Ridom Spa Server.
    :type string
    
    :returns: Absolute path to sparepeats.fasta file downloaded.
     
    """    
    # check if file is available in folder provided
    reps = os.path.join(folder, 'sparepeats.fasta')

    ## timestamp name
    filename_stamp = folder + '/.success'
        
    ## check if previously exists
    if os.path.exists(reps):
        ## check if previously timestamp generated
        if os.path.isfile(filename_stamp):
            stamp = read_time_stamp(filename_stamp)
            print ("\tA previous download created sparepeats.fasta on: %s" %stamp)
    else:
        # downloads
        urllib.request.urlretrieve('http://spa.ridom.de/dynamic/sparepeats.fasta', reps)
    
    ## check if correctly download
    if os.path.exists(reps):
        print_time_stamp(filename_stamp)
    else:
        sys.exit('Could not download http://spa.ridom.de/dynamic/sparepeats.fasta, download manually and use -p flag')

    ## returns    
    return (reps)

####################################################
def download_file_types(folder):
    """
    Downloads spa types file from SeqNet/Ridom Spa Server.
    
    Given a folder absolute path ``folder``, it initially checks if file :file:`spatypes.txt` is
    available. It checks for a timestamp previosuly generated and returns if it is available. If file
    is not accessible it tries to download it from url site: http://spa.ridom.de/dynamic/spatypes.txt
    
    :param folder: Absolute path to folder containing SeqNet/Ridom Spa Server.
    :type string
    
    :returns: Absolute path to spatypes.txt file downloaded.
     
    """    
    # check if file is available in folder provided
    orders = os.path.join(folder, 'spatypes.txt')

    ## timestamp name
    filename_stamp = folder + '/.success'
        
    ## check if previously exists
    if os.path.exists(orders):
        ## check if previously timestamp generated
        if os.path.isfile(filename_stamp):
            stamp = read_time_stamp(filename_stamp)
            print ("\tA previous download created spatypes.txt on: %s" %stamp)
    else:
        # downloads
        urllib.request.urlretrieve('http://spa.ridom.de/dynamic/spatypes.txt', orders)
    
    ## check if correctly download
    if os.path.exists(orders):
        print_time_stamp(filename_stamp)
    else:
        sys.exit('Could not download http://spa.ridom.de/dynamic/spatypes.txt, download manually and use -p flag')

    ## returns    
    return (orders)

####################################################
def print_time_stamp (out):
    """Prints out timestamp in a file provided. Format: time.time()"""
    timefile = open(out, 'w')    
    string2write = str(time.time())
    timefile.write(string2write)
    return()

####################################################
def read_time_stamp (out):
    """Reads timestamp from a file provided. Format: time.time()"""
    st_hd = open(out, 'r')
    st = st_hd.read()
    st_hd.close()
    stamp = datetime.fromtimestamp(float(st)).strftime('%Y-%m-%d %H:%M:%S')
    return(stamp)