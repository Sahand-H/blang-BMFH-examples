# Setup working directory
samples_folder = paste("Desktop/blang/blang-BMFH-examples/",model_name,"/results/samples/",sep = "")

# Enter Name of random variable & model here:
rvar_name = ""
model_name= ""


# Read .csv file and initial histogram plotting (+ legend)
vals <- read.csv(paste(samples_folder,rvar_name,".csv", sep = ""))

hist(vals$value, probability = TRUE, col = "cornflowerblue", xlim = range(0,1), 
     main = paste("PDF of", rvar_name), xlab = paste("Value of", rvar_name))

legend("topright", lwd = 10, c("posterior distribution"), col = "cornflowerblue")
