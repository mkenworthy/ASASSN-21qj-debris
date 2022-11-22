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
        "src/data/asassn/light_curve_a4748464-dd11-4557-ae7f-6c50774aa532.csv"
     output:
        "src/data/obs_ASASSN.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_asassn.py"
rule proc_neowise:
     input:
        "src/data/neowise/ASASSN-21qj_2013-2022.tbl"
     output:
        "src/data/obs_NEOWISE.ecsv"
     conda:
        "environment.yml"
     script:
        "src/scripts/convert_neowise.py"
rule proc_aavso:
     input:
        "src/data/aavso/aavsodata_636cdb53c895b.txt"
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
        "src/tex/output/collision_epoch_text.txt", "src/tex/output/t_duration.txt", "src/tex/output/t_after.txt", "src/tex/output/t_before.txt"
    conda:
        "environment.yml"
    script:
        "src/scripts/calc_neowise_properties.py"
