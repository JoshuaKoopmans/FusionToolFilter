def process_fusion_catcher():

    with open("tests/test_dependencies/final-list_candidate-fusion-genes.tsv", "r") as f:
        file_content = f.readlines()
    f.close()
    return file_content[:4]
