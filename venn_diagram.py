!pip install matplotlib matplotlib_venn
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

A = {'a','b','c','k','m','n','p','q','r','v','w','x'}
B = {'d','e','f','k','m','n','s','t','u','v','w','x'}
C = {'g','h','j','p','q','r','s','t','u','v','w','x'}

venn = venn3([A, B, C], ('A', 'B', 'C'))

venn3_circles([A, B, C])


venn.get_label_by_id('100').set_text(','.join(sorted(A - B - C)))  # Only in A
venn.get_label_by_id('010').set_text(','.join(sorted(B - A - C)))  # Only in B
venn.get_label_by_id('001').set_text(','.join(sorted(C - A - B)))  # Only in C
venn.get_label_by_id('110').set_text(','.join(sorted(A & B - C)))  # A & B, not C
venn.get_label_by_id('101').set_text(','.join(sorted(A & C - B)))  # A & C, not B
venn.get_label_by_id('011').set_text(','.join(sorted(B & C - A)))  # B & C, not A
venn.get_label_by_id('111').set_text(','.join(sorted(A & B & C)))  # A & B & C


plt.show()
