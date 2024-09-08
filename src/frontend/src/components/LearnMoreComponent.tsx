import {
  CloudArrowUpIcon,
  LockClosedIcon,
  ServerIcon,
} from "@heroicons/react/20/solid";

export default function LearnMoreComponent() {
  return (
    <div className="relative isolate overflow-hidden bg-white">
      <div
        aria-hidden="true"
        className="absolute -top-80 left-[max(6rem,33%)] -z-10 transform-gpu blur-3xl sm:left-1/2 md:top-20 lg:ml-20 xl:top-3 xl:ml-56"
      >
        <div
          style={{
            clipPath:
              "polygon(63.1% 29.6%, 100% 17.2%, 76.7% 3.1%, 48.4% 0.1%, 44.6% 4.8%, 54.5% 25.4%, 59.8% 49.1%, 55.3% 57.9%, 44.5% 57.3%, 27.8% 48%, 35.1% 81.6%, 0% 97.8%, 39.3% 100%, 35.3% 81.5%, 97.2% 52.8%, 63.1% 29.6%)",
          }}
          className="aspect-[801/1036] w-[50.0625rem] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30"
        />
      </div>
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl lg:mx-0">
          <p className="text-lg font-semibold leading-8 tracking-tight text-lime-700">
            Find reliable solutions faster !
          </p>
          <h1 className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Learn More About Our Platform
          </h1>
          <p className="mt-6 text-xl leading-8 text-gray-700">
            Navigating legal matters can be overwhelming, especially when you’re
            unsure whether you need a lawyer or how to find the right one.
            That’s where we come in. Our platform is designed to simplify the
            process of identifying your legal needs and connecting you with
            qualified legal professionals. Whether you're dealing with a
            business contract, family issue, or intellectual property matter,
            we’re here to guide you every step of the way.
          </p>
        </div>
        <div className="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 lg:mx-0 lg:mt-10 lg:max-w-none lg:grid-cols-12">
          <div className="relative lg:order-last lg:col-span-5">
            <svg
              aria-hidden="true"
              className="absolute -top-[40rem] left-1 -z-10 h-[64rem] w-[175.5rem] -translate-x-1/2 stroke-gray-900/10 [mask-image:radial-gradient(64rem_64rem_at_111.5rem_0%,white,transparent)]"
            >
              <defs>
                <pattern
                  id="e87443c8-56e4-4c20-9111-55b82fa704e3"
                  width={200}
                  height={200}
                  patternUnits="userSpaceOnUse"
                >
                  <path d="M0.5 0V200M200 0.5L0 0.499983" />
                </pattern>
              </defs>
              <rect
                fill="url(#e87443c8-56e4-4c20-9111-55b82fa704e3)"
                width="100%"
                height="100%"
                strokeWidth={0}
              />
            </svg>
            <figure className="border-l border-indigo-600 pl-8">
              <blockquote className="text-xl font-semibold leading-8 tracking-tight text-gray-900">
                <p>
                  “LawyerUp really helped me when I needed to form a partnership
                  for my small business! I was struggling to find a qualified
                  attorney in my area, but LawyerUp made this process seamless.”
                </p>
              </blockquote>
              <figcaption className="mt-8 flex gap-x-4">
                <img
                  alt=""
                  src="https://media.licdn.com/dms/image/v2/C4E03AQEq5JwFQFcAog/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1579149074676?e=1731542400&v=beta&t=_DqelY2o6jlILWmfN7P8cHTnVpyYgE1swPG3T3lwIKg"
                  className="mt-1 h-10 w-10 flex-none rounded-full bg-gray-50"
                />
                <div className="text-sm leading-6">
                  <div className="font-semibold text-gray-900">Emily Chan</div>
                  <div className="text-gray-600">@itsanemily</div>
                </div>
              </figcaption>
            </figure>
            <div className="mt-10 flex items-center gap-x-6">
              <a
                href="/result"
                className="rounded-md bg-lime-700 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-lime-800 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Get started
              </a>
            </div>
          </div>
          <div className="max-w-xl text-base leading-7 text-gray-700 lg:col-span-7">
            <div className="text-3xl text-black">
              <p>How It Works</p>
            </div>
            <ul role="list" className="mt-8 max-w-xl space-y-8 text-gray-600">
              <li className="flex gap-x-3">
                <CloudArrowUpIcon
                  aria-hidden="true"
                  className="mt-1 h-5 w-5 flex-none text-lime-700"
                />
                <span>
                  <strong className="font-semibold text-gray-900">
                    Assess Your Situation
                  </strong>{" "}
                  Answer a few simple questions to determine whether legal
                  assistance is necessary for your case.
                </span>
              </li>
              <li className="flex gap-x-3">
                <LockClosedIcon
                  aria-hidden="true"
                  className="mt-1 h-5 w-5 flex-none text-lime-700"
                />
                <span>
                  <strong className="font-semibold text-gray-900">
                    Get Personalized Recommendations
                  </strong>{" "}
                  Based on your responses, we’ll match you with experienced
                  lawyers in your area who specialize in the specific type of
                  law you need.
                </span>
              </li>
              <li className="flex gap-x-3">
                <ServerIcon
                  aria-hidden="true"
                  className="mt-1 h-5 w-5 flex-none text-lime-700"
                />
                <span>
                  <strong className="font-semibold text-gray-900">
                    Connect With Experts
                  </strong>{" "}
                  Review lawyer profiles, compare expertise, and choose the
                  attorney who best fits your needs.
                </span>
              </li>
            </ul>
            <div className="text-3xl mt-8 text-black">
              <p>Why Choose Us?</p>
            </div>
            <ul role="list" className="mt-8 max-w-xl space-y-8 text-gray-600">
              <li className="flex gap-x-3">
                <CloudArrowUpIcon
                  aria-hidden="true"
                  className="mt-1 h-5 w-5 flex-none text-lime-700"
                />
                <span>
                  <strong className="font-semibold text-gray-900">
                    Tailored Legal Matches
                  </strong>{" "}
                  We connect you with attorneys who have expertise in your
                  unique legal issue, ensuring you get the right help.
                </span>
              </li>
              <li className="flex gap-x-3">
                <LockClosedIcon
                  aria-hidden="true"
                  className="mt-1 h-5 w-5 flex-none text-lime-700"
                />
                <span>
                  <strong className="font-semibold text-gray-900">
                    User-Friendly{" "}
                  </strong>{" "}
                  Our platform is designed to be simple, intuitive, and
                  stress-free, so you can quickly find the guidance you need.
                </span>
              </li>
              <li className="flex gap-x-3">
                <ServerIcon
                  aria-hidden="true"
                  className="mt-1 h-5 w-5 flex-none text-lime-700"
                />
                <span>
                  <strong className="font-semibold text-gray-900">
                    Trusted Lawyers
                  </strong>{" "}
                  We vet all lawyers on our platform to ensure they meet high
                  standards of professionalism and experience.
                </span>
              </li>
            </ul>
            <h2 className="mt-16 text-2xl font-bold tracking-tight text-gray-900">
              No Lawyer? No problem.
            </h2>
            <p className="mt-6">
              Whether you’re looking to protect your rights, resolve a legal
              dispute, or simply get advice, our platform is the first step to
              finding the right lawyer for you.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
