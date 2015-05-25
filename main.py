from lxml import html
import requests

def main():
  page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
  tree = html.fromstring(page.text)
  
  .col3/table[1]/tbody
  
  for tablerow as tr:
    if(tr.td[0] hasClass tableheading)
      month = tr.td[0]
      year = tr.td[1]
      
      for i = 2; i < tr.td.size; i++
        eventTypes[i-2] = tr.td[i].content
      
    else
      day = tr.td[1]
      
      for(i = 2; i < tr.td.size; i++)
        if(tr.td[i] != "")
          events[] = {
            name = tr.td[i]
            type = eventTypes[i-2]
            eventDate = day+month+year
          }

  cal = icalendar.Calendar()
  cal.add('prodid', '-//Serpentine Events Calendar//serpentine.org.uk//')
  cal.add('version', '2.0')
  
  # now create an event for each link
  for link in links:
    try:
      event = icalendar.Event()
      event['uid'] = "%s@serp" % linkdata['id']
      event.add('summary', event_title)
      event.add('dtstart', event_date)
      event.add('dtend', event_date + datetime.timedelta(1))
      event.add('organizer', linkdata['author'])
      event.add('url', linkdata['url'])
      cal.add_component(event)
    except:
      pass
  return cal.to_ical() # content_type="text/calendar")
try:
  import webapp2

  class MainPage(webapp2.RequestHandler):
    def get(self):
      self.response.headers['Content-Type'] = 'text/calendar'
      cal = main()
      self.response.out.write(cal)
      
  app = webapp2.WSGIApplication([('/', MainPage)])
except:
    pass

if __name__ == '__main__':
    print main()
