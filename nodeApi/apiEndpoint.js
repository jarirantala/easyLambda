'use strict';

module.exports.handler = (event, context, callback) => {
  const response = {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Good job! Your serverless function executed successfully!',
      input: event,
    }),
  };

  callback(null, response);
};
