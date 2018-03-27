Some notes on the analytical approach and code snippets used through the task



Data Transformation:
Dimensionality Reduction Process:

Entries of city dim transferred through these steps:

1- any egyptian street, district or city is transferred to one of 27 egyptian governorates entries.
2- any entries with more than one governorate input is transferred to one entry "Many Governorates"
3- North and South Sinai Governorates are reduced to one input "Sinai"
4- remote, online, work from home entries are transferred to one entry "Work From Home"
5- any place outside Egypt geo locations are transferred to "International" and that has been done with several processes
a- first, the locations with clear identification of a place outside egypt territory are transferred to "International"
b- second, the locations that have no clear identification that possess entries such as "any, everywhere, any place, any provenance, or similar words that don't provide clear identification of a place" are transferred into "International" or "Many Governorates" based on the entries from currency dimension


Entries of required experience dim transferred through these steps:

1- standardizing the entries on these values 
t
t1:t2
+t
-t

2- any entries with rather than this standard were transferred into the standardized format and removing any extra characters

3- the standard can’t involve differentiation between information such as; “more than or equal” and “more than”, “less than or equal” and “less than”.
All the entries that involve of inclusion or exclusion info are treated as inclusion information

4- all the steps before are changed into this:
A- the experience required field will be splitted into two fields “min_experience” “max_experience”
For cells of fixed years of experience i.e. not range values will be transferred to t:t
For cells of more than and less than will be considered like this:
Conventionally start point is 0 and end point is 55 so if >t will be t:55 and <t will be 0:t


Entries of Job Category and Job Industry:

“Select” transferred to null values
