#FROM is the base image for which we will run our application
FROM node:alpine

# Working Directory of our Application
WORKDIR /app

# Copy Dependencies
COPY package.json /app

# Install yarn?
RUN yarn install

# Copy App Over
COPY .. /app

# Start app?
CMD ["yarn", "run", "start"]