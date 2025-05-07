import spacy
import os

if __name__ == "__main__":
    arrayId = os.environ.get( 'SLURM_ARRAY_TASK_ID', None )

    if arrayId is None:
        print( "This script should be run as a SLURM array job." )
        exit( 1 )
    
    arrayIndex = int(arrayId)
    print( f"Running SLURM array job with ID: {arrayId}" )

    with open( f"input/input-{arrayIndex:02d}.txt", "r" ) as input:
        with open( f"output/output-{arrayIndex:02d}.txt", "w" ) as output:
        
            nlp = spacy.load( "en_core_web_sm" )

            print( f"Processing file: input-{arrayIndex:02d}.txt" )
            doc = nlp( input.read() )
            for token in doc:
                output.writelines( f"{token.text}\t{token.pos_}\t{token.dep_}\n" )

    print( f"Finished processing file: input-{arrayIndex:02d}.txt" )
    print( f"Output written to: output/output-{arrayIndex:02d}.txt" )
    