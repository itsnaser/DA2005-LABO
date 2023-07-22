class DnaSeq:
    def __init__(self, accession: str, seq: str):
        '''
        Creates a DnaSeq object

        :param accession: name of the DnaSeq
        :type accession: str
        :param seq: DnaSeq sequence
        :type seq: str
        '''
        # deny empty accession or seq
        if accession in [None, ""] or seq in [None, ""]:
            raise ValueError
        self.seq = seq
        self.accession = accession

    def __len__(self):
        '''
        Returns length of the DnaSeq

        :return: length of the self.seq
        :rtype: int
        '''
        return len(self.seq)

    def __str__(self):
        '''
        Returns name of the DnaSeq

        :return: self.accession
        :rtype: str
        '''
        return f"<DnaSeq accession='{self.accession}'>"


def read_dna(filename: str) -> list:
    '''
    Read DNA names and sequences from a (.fa, .txt) file

    :param filename: name of the file
    :type filename: str
    :return: list of DnaSeq objects from a file
    :rtype: list of DnaSeq instances
    '''
    # raise a FileNotFoundError error if the file is not found
    try:
        f = open(filename, 'r')
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError

    dnaseq_list = []
    # loop through the file lines
    for i in range(len(lines)):
        accession = lines[i]  # assign line of number i to accession
        # assign line of number i+1 to seq,
        # if total lines of the file are less than the i+1
        seq = lines[i+1] if i+1 < len(lines) else ""

        # validate accession, remove ">" and remove any spaces from seq
        if accession.startswith(">") and seq.strip() != "":
            accession = accession.strip().replace(">", "")
            seq = seq.strip()
            dnaseq_object = DnaSeq(accession, seq)
            dnaseq_list.append(dnaseq_object)

    return dnaseq_list


def check_exact_overlap(dna1: DnaSeq, dna2: DnaSeq, overlap: int = 10) -> int:
    '''
    Checks overlap between two DnaSeq instances

    :param dna1: DnaSeq 1, check if its end overlaps with the start of dna2
    :type dna1: DnaSeq object
    :param dna2: DnaSeq 2, check if its start overlaps with the end of dna1
    :type dna2: DnaSeq object
    :param overlap: default value of minimum overlap
    :type overlap: int
    :return: length of the overlapped part of two sequences
    :rtype: int
    '''
    seq1 = dna1.seq
    seq2 = dna2.seq
    seq1_length = len(seq1)
    overlap_count = 0
    # same seq comparison is not allowed
    if seq1 == seq2:
        return 0
    # loop through the length of the first sequence
    # slice the sequence from i to the end of it
    # compeare if the second sequence starts with the sliced sequence
    # if true, break and return the length of the overlapped part
    for i in range(seq1_length):
        suff = seq1[i:]
        if seq2.startswith(suff):
            overlap_count = len(suff)
            break
    return overlap_count if (overlap_count >= overlap) else 0


def overlaps(dnaseq_list: list, check_exact_overlap) -> dict:
    '''
    Checks if Dna sequences overlap with each other in the list

    :param dnaseq_list: list of the Dna sequences
    :type dnaseq_list: list of DnaSeq instances
    :param check_exact_overlap: function to validate the overlap
    :type check_exact_overlap: function
    :return: dictionary of dictionaries inlcudes each DnaSeq
    with all the overlapped DnaSeq and length of the overlap
    e.g. {'accession':{'accession':3,'accession':4},'accession':{'accession':5}
    :rtype: dict
    '''
    dict_of_overlapped_seq: dict = {}
    # nested loop to compare each DnaSeq with all other DnaSeq instances
    for dna_obj1 in dnaseq_list:
        for dna_obj2 in dnaseq_list:
            overlap = check_exact_overlap(dna_obj1, dna_obj2)
            if overlap != 0:
                # if the key exists, then add a new key:value to it
                # otherwise create a new key
                if dict_of_overlapped_seq.get(dna_obj1.accession):
                    dict_of_overlapped_seq[dna_obj1.accession].update({
                        dna_obj2.accession: overlap})
                else:
                    dict_of_overlapped_seq[dna_obj1.accession] = {
                        dna_obj2.accession: overlap}
    return dict_of_overlapped_seq

#
# Testing code. You should not change any code below here. To run the tests
# uncomment the last line in the file.
#


def test_class_DnaSeq():
    s1 = DnaSeq('s1', 'ACGT')
    s2 = DnaSeq(
        's2', 'ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT')
    assert len(s1) == 4, 'Your length method (__len__) is not correct.'
    assert len(s2) == 70, 'Your length method (__len__) is not correct.'

    assert str(
        s1) == "<DnaSeq accession='s1'>", 'The __str__ method is not following the specification.'
    assert str(
        s2) == "<DnaSeq accession='s2'>", 'The __str__ method is not following the specification.'

    # The rest of this function is verifying that we are indeed raising an exception.
    status = 0
    try:
        s3 = DnaSeq('', 'ACGT')
    except ValueError:
        status += 1
    try:
        s3 = DnaSeq('s3', None)
    except ValueError:
        status += 1

    try:
        s3 = DnaSeq(None, '')
    except ValueError:
        status += 1
    if status != 3:
        raise Exception('class DnaSeq does not raise a ValueError '
                        'exception with initialised with empty '
                        'accession and sequence.')
    print('DnaSeq passed')


def test_reading():
    dna1 = read_dna('ex1.fa')
    assert len(
        dna1) == 6, 'The file "ex1.fa" has exactly 6 sequences, but your code does not return that.'
    assert list(map(lambda x: x.accession, dna1)) == [
        f's{i}' for i in range(6)], 'The accessions are not read correctly'

    dna2 = read_dna('ex2.fa')
    assert len(
        dna2) == 6, 'The file "ex2.fa" has exactly 6 sequences, but your code does not return that.'

    covid = read_dna('sars_cov_2.fa')
    assert len(
        covid[0].seq) == 29903, 'The length of the genome in "sars_cov_2.fa" is 29903, but your code does not return that.'

    print('read_dna passed')


def test_overlap():
    s0 = DnaSeq('s0', 'AAACCC')
    s1 = DnaSeq('s1', 'CCCGGG')
    s2 = DnaSeq('s2', 'TTTTCC')
    s3 = DnaSeq('s3', 'CCAGGG')
    s4 = DnaSeq('s4', 'GGGGGGGGAAAGGGGG')
    s5 = DnaSeq('s5', 'AAATTTTTTTTTTTTTTTTTTT')

    data1 = [s0, s1, s2, s3]
    assert check_exact_overlap(s0, s1, 2) == 3
    assert check_exact_overlap(s0, s1) == 0
    assert check_exact_overlap(s0, s3, 2) == 2
    assert check_exact_overlap(s1, s2, 2) == 0
    assert check_exact_overlap(s2, s1, 2) == 2
    assert check_exact_overlap(s2, s3, 2) == 2
    assert check_exact_overlap(
        s4, s5, 1) == 0, 'Do not allow "internal" substrings to overlap. s4 and s5 does not have an overlap.'
    assert check_exact_overlap(s4, s5, 2) == 0
    assert check_exact_overlap(s4, s5, 3) == 0

    res0 = overlaps(data1, lambda s1, s2: check_exact_overlap(s1, s2, 2))
    assert len(res0) == 2, 'You get the wrong number of overlaps'
    assert res0 == {'s0': {'s1': 3, 's3': 2}, 's2': {'s1': 2, 's3': 2}}

    dna_data = read_dna('ex1.fa')
    res1 = overlaps(dna_data, check_exact_overlap)
    assert len(res1) == 5
    for left, right in [('s0', 's1'), ('s1', 's2'), ('s2', 's3'), ('s3', 's4'),
                        ('s4', 's5')]:
        assert res1[left][right], f'Missing overlap of {left} and {right} (in that order)'
    print('overlap code passed')


def test_all():
    test_class_DnaSeq()
    test_reading()
    test_overlap()
    print('Yay, all good')


# Uncomment this to test everything:
if __name__ == '__main__':
    test_all()
