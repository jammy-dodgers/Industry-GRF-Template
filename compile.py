import glob, os, subprocess

header = "./src/header.nml"
cargos = "./src/cargos.nml"
cargo_folder = "./src/cargos/*.nml"
industry_folder = "./src/industries/*.nml"
cache_nml_file = "./.cache/output.nml"

grf_name = os.path.basename(os.getcwd())

def flatten(xss):
    return [x for xs in xss for x in xs]

if not os.path.isdir(".cache"):
    os.mkdir(".cache")

with open(cache_nml_file, 'w') as output:
    for file in flatten([[header, cargos], glob.glob(cargo_folder), glob.glob(industry_folder)]):
        print(file)
        with open(file) as input:
            for line in input:
                output.write(line)
            output.write('\n')

tmp_grf_path = "./.cache/{}.grf".format(grf_name)
if os.path.exists(tmp_grf_path):
    os.remove(tmp_grf_path)

subprocess.run("./nmlc.exe --grf .{} ../.cache/output.nml".format(tmp_grf_path), cwd="./src")