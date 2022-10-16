rule proc_atlas:
     input:
        "src/data/atlas/job211831.txt"
     output:
        "src/data/obs_ATLAS.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_atlas.py"
rule proc_asassn:
     input:
        "src/data/asassn/light_curve_f51db35b-11b8-4840-a6d9-979a455d6978.csv"
     output:
        "src/data/obs_ASASSN.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_asassn.py"
rule proc_neowise:
     input:
        "src/data/neowise/ASASSN-21qj_2013-2021.tbl"
     output:
        "src/data/obs_NEOWISE.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_neowise.py"
rule proc_aavso:
     input:
        "src/data/aavso/aavsodata_62f60478b309b.txt"
     output:
        "src/data/obs_AAVSO.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_aavso.py"
rule calc_epochs_of_collision:
    input:
        "src/data/obs_NEOWISE.ecsv"
    output:
        "src/tex/output/collision_epoch_text.txt"
        "src/tex/output/t_duration.txt"
    conda:
        "environment.yml"
    script:
        "src/scripts/calc_neowise_properties.py"
