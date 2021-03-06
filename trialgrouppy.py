import pandas as pd
df = pd.read_csv('trialgroup.csv', sep=',')
colums = ['Species', 'LocalID', 'Domain']

for row in df.iterrows():

    #searchfor = ['Acidianus', 'Acidilobus', 'Acidiplasma','Acidococcus','Aciduliprofundum','Aeropyrum','Archaeoglobus','Bacilloviridae','Caldisphaera','Caldivirga','Caldococcus','Cenarchaeum','Desulfurococcus','Ferroglobus','Ferroplasma','Geogemma','Geoglobus','Haladaptatus','Halalkalicoccus','Haloalcalophilium','Haloarcula','Halobacterium','Halobaculum','Halobiforma','Halococcus','Haloferax','Halogeometricum','Halomicrobium','Halopiger','Haloplanus','Haloquadratum','Halorhabdus','Halorubrum','Halosarcina','Halosimplex','Halostagnicola','Haloterrigena','Halovivax','Hyperthermus','Ignicoccus','Ignisphaera','Metallosphaera','Methanimicrococcus','Methanobacterium','Methanobrevibacter','Methanocalculus','Methanocaldococcus','Methanocella','Methanococcoides','Methanococcus','Methanocorpusculum','Methanoculleus','Methanofollis','Methanogenium','Methanohalobium','Methanohalophilus','Methanolacinia','Methanolobus','Methanomethylovorans','Methanomicrobium','Methanoplanus','Methanopyrus','Methanoregula','Methanosaeta','Methanosalsum','Methanosarcina','Methanosphaera','Methanospirillum','Methanothermobacter','Methanothermococcus','Methanothermus','Methanothrix','Methanotorris','Nanoarchaeum','Natrialba','Natrinema','Natronobacterium','Natronococcus','Natronolimnobius','Natronomonas','Natronorubrum','Nitrosopumilus','Palaeococcus','Picrophilus','Pyrobaculum','Pyrococcus','Pyrodictium','Pyrolobus','Staphylothermus','Stetteria','Stygiolobus','Sulfolobus','Sulfophobococcus','Sulfurisphaera','Thermocladium','Thermococcus','Thermodiscus','Thermofilum','Thermoplasma','Thermoproteus','Thermosphaera','Vulcanisaeta']
    



    if df[df['Species'].str.contains('Acidianus', 'Acidilobus', 'Acidiplasma','Acidococcus','Aciduliprofundum','Aeropyrum','Archaeoglobus','Bacilloviridae','Caldisphaera','Caldivirga','Caldococcus','Cenarchaeum','Desulfurococcus','Ferroglobus','Ferroplasma','Geogemma','Geoglobus','Haladaptatus','Halalkalicoccus','Haloalcalophilium','Haloarcula','Halobacterium','Halobaculum','Halobiforma','Halococcus','Haloferax','Halogeometricum','Halomicrobium','Halopiger','Haloplanus','Haloquadratum','Halorhabdus','Halorubrum','Halosarcina','Halosimplex','Halostagnicola','Haloterrigena','Halovivax','Hyperthermus','Ignicoccus','Ignisphaera','Metallosphaera','Methanimicrococcus','Methanobacterium','Methanobrevibacter','Methanocalculus','Methanocaldococcus','Methanocella','Methanococcoides','Methanococcus','Methanocorpusculum','Methanoculleus','Methanofollis','Methanogenium','Methanohalobium','Methanohalophilus','Methanolacinia','Methanolobus','Methanomethylovorans','Methanomicrobium','Methanoplanus','Methanopyrus','Methanoregula','Methanosaeta','Methanosalsum','Methanosarcina','Methanosphaera','Methanospirillum','Methanothermobacter','Methanothermococcus','Methanothermus','Methanothrix','Methanotorris','Nanoarchaeum','Natrialba','Natrinema','Natronobacterium','Natronococcus','Natronolimnobius','Natronomonas','Natronorubrum','Nitrosopumilus','Palaeococcus','Picrophilus','Pyrobaculum','Pyrococcus','Pyrodictium','Pyrolobus','Staphylothermus','Stetteria','Stygiolobus','Sulfolobus','Sulfophobococcus','Sulfurisphaera','Thermocladium','Thermococcus','Thermodiscus','Thermofilum','Thermoplasma','Thermoproteus','Thermosphaera','Vulcanisaeta')]:
        df['Domain'] = 'Archaea'




    else:
        df['Domain'] = 'Bacteria'

print pd.df