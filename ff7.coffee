_       = require "lodash"
fs      = require "fs"
Twitter = require "twitter"

client = new Twitter
  consumer_key:         process.env.FF7_CONSUMER_KEY
  consumer_secret:      process.env.FF7_CONSUMER_SECRET
  access_token_key:     process.env.FF7_ACCESS_TOKEN_KEY
  access_token_secret:  process.env.FF7_ACCESS_TOKEN_SECRET


module.exports = ->

  # No real need for async operations...
  # This file is running once an hour, let's make things more readable instead
  script = fs.readFileSync("#{__dirname}/quotes.txt", { encoding: "utf8" })

  hold = ""
  skip = false

  # Create full sentences from a slightly malformed FF7 script
  script = _.reduceRight script.split("\n"), (result, line) ->
    skip = false
    line = line.trim()
    if (_.uniq line).length < 2 then return result

    # Wait until we hit the beginning of a sentence to push these fragments
    if line.charAt(0).match(/[a-z]/)
      hold += line
      skip = true
      return result

    # Finally we have a real sentence, let's make it a choice
    if line + hold >= 139 then return result
    result.push "#{line} #{hold}".trim()
    hold = ""

    return result
  , []

  tweet = { status: (_.sample script) }

  client.post "/statuses/update", tweet, (err, tweet, response) ->
    console.log err, tweet, response
    process.exit 0


